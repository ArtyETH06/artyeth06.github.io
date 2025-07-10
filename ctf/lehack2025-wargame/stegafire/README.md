# Wargame: StegaFire

StegaFire is a challenge proposed during the famous **leHack Wargame CTF**.  
I flagged this challenge with one of my main teammates for this CTF: Juliusxd23.

*(I don’t have all screenshots because they shut down the infrastructure before I could make this report, but don’t worry, I got everything in my head x))*  

This WU is divided into 3 parts:  
- What we have  
- The solution  
- Follow the white rabbit (You better don't actually)  

---

## What we have ?

At first, we arrive on a page with a simple `Start` button.  
When pressing it, an animation of **flames** appears at the bottom of the screen, and we can also hear **notes** being played at various frequencies.

By looking at the code, we quickly noticed that no sound files were being loaded.  
That means the sound must be generated directly from the code.  
After a bit of research, we found this function:  

```js
function playRandomRetroSound() {
    const synth = new Tone.Synth({
        oscillator: { type: 'square' }
    }).toDestination();
    const now = Tone.now();
    const note = ['C4', 'E4', 'G4', 'B4', 'D4', 'F4', 'A4', 'C5', 'E5', 'G5', 'B5', 'D5', 'F5', 'A5', 'C6', 'E6'][Math.floor(Math.random() * 16)];
    synth.triggerAttackRelease(note, '8n', now);
    setTimeout(playRandomRetroSound, Math.random() * 3000 + 2000);
}
```

This confirmed that the sounds were randomly generated.  
(We double-checked by launching two instances of the website at the same time — no synchro in sounds.)

By digging into the main file `fire.js`, we noticed something odd:  
A **Konami Code** was implemented (it's a famous cheat code used in many games — [More here](https://fr.wikipedia.org/wiki/Code_Konami)):

```js
let konamiCode = ["ArrowUp", "ArrowUp", "ArrowDown", "ArrowDown", "ArrowLeft", "ArrowRight", "ArrowLeft", "ArrowRight", "b", "a"];
```

When inputting this exact sequence, the **ChillMode** gets activated:

```js
function handleKonamiCode(event) {
    if (event.key === konamiCode[konamiIndex]) {
        konamiIndex++;
        if (konamiIndex === konamiCode.length) {
            toggleChillMode();
            konamiIndex = 0;
        }
    } else {
        konamiIndex = 0;
    }
}
```

Basically, it changes the color theme of the interface and (maybe) changes the sounds — we weren’t even sure at that point.

We also found two interesting files:  
- `fire.js.map`  
- `fire.ts`  

These files seemed to be the core of the challenge, which makes sense given the name: **Stega-Fire**.

## So... where are we going?

Here’s where it gets really weird (shout out to Julius for finding this completely by accident 👀).

There are **two copies** of the file `fire.min.js.map` located at **two different paths**:

-  `https://stega-fire.wargame.rocks/js/fire.min.js.map`  
-  `https://stega-fire.wargame.rocks/fire.min.js.map`  

*(For people who lost neurones due to the wargame: one is in `/`, the other is in `/js` directory.)*  

We found it **super suspicious** that the same file exists in two places... until we checked their sizes.  
Result? They differ by **exactly one byte.**  

![](https://raw.githubusercontent.com/ArtyETH06/artyeth06.github.io/main/ctf/lehack2025-wargame/stegafire/images/Pasted%20image%2020250630095256.png)

This was a **huge hint.** (Later, the challenge maker told us this difference wasn’t intentional — they were supposed to be identical.)


### 🔍 Diff Time

We uploaded both files to [Diffchecker](https://www.diffchecker.com/) to compare them.

The differences were **small but visible** — sometimes a capital letter, sometimes a number, bracket, or underscore.

![](https://raw.githubusercontent.com/ArtyETH06/artyeth06.github.io/main/ctf/lehack2025-wargame/stegafire/images/Pasted%20image%2020250630101148.png)

By extracting the changing characters in order, it slowly started forming the flag:  
→ `Le`, then `LeHack`, and continuing...

![](https://raw.githubusercontent.com/ArtyETH06/artyeth06.github.io/main/ctf/lehack2025-wargame/stegafire/images/Pasted%20image%2020250630101548.png)
And by indentifying the lettters/numbers/brackets/underscores that changes from one file to the other,we have the flag: `LeHACK{83_CaR3fUL_F1R3_8URn2}` ✅🔥

This seems pretty easy once you have found that, but we went through a lot of things first...
Let's find out !


## Follow the White Rabbit (You really shouldn't...)

### 🔥 The Real Challenge

The real difficulty wasn’t finding the differences *once we had both files*... but **figuring out that the challenge was about comparing them in the first place.**

It took us **over 3 hours** to realize that.

### 🎶 The Sounds Rabbit Hole

Early on, we thought the **random notes** had something to do with the flag — maybe some encoded frequencies?  

We recorded the sounds, tried to run some analysis , etc... **→ Nothing.**  

At some point, we even considered reconstructing spectrograms by matching frequencies to image lines... **→ Full dead end.**  

But remember,the sounds are generated in a random patern,so nothing about this could be useful

![](https://raw.githubusercontent.com/ArtyETH06/artyeth06.github.io/main/ctf/lehack2025-wargame/stegafire/images/Pasted%20image%2020250630103946.png)

### 🔥 The Fire Rabbit Hole

There was also the flame animation at the bottom of the screen.  
We assumed that maybe the flag was hidden in the **pixel colors**.

Here’s part of the function that generates colors:

```ts
function valueToColor(value: number): [number, number, number] {
    if (isChillMode) {
        const chillPalette = [/* ... color values ... */];
        return chillPalette[value] || [0, 0, 0];
    }

    const palette = [/* ... color values ... */];
    return palette[value] || [0, 0, 0];
}
```

→ **Spoiler:** Nope. This was just for the color palette of normal mode vs chill mode. No hidden data there.

![](https://raw.githubusercontent.com/ArtyETH06/artyeth06.github.io/main/ctf/lehack2025-wargame/stegafire/images/Pasted%20image%2020250630102322.png)

### 📜 TypeScript, A.K.A whaT the fuck is this Shit

There was a `fire.ts` file — a TypeScript version of `fire.js`.  
The challenge author hinted that the TS file might be useful because the JS on the page wasn’t "complete".Underlying the fact that the `fire.js` file might not be complete and that we can find some more information in the `fire.ts`...

→ We tried recompiling TS → JS, running it locally, patching it, etc... **Nothing.**  

In hindsight... either the challenge author was trolling us (likely) or just wasn’t sober (very likely 🍺).

## Conclusion: Why tho?

After solving the challenge and talking with the challenge maker, the answer was simple:  

→ **All of this: the fire, the sounds, the Konami code... was just a giant rabbit hole.**  

A massive troll designed to waste time — and it worked.  
Shout out to the creator for this inspitation , though... that was fun (once it was over).

![](https://raw.githubusercontent.com/ArtyETH06/artyeth06.github.io/main/ctf/lehack2025-wargame/stegafire/images/Pasted%20image%2020250630103759.png)



## Stats

As far as we know, only **3 teams (out of 300+)** managed to flag this challenge.  
We were **really proud** of this, even though we missed the **First Blood** by just **4 minutes**...

The CTFd scoreboard looked something like this:

```plaintext
CTFd Scores:
Pepito:         12:30 PM
XXX:            12:33 PM
EternalBLue (us): 12:34 PM
```


![](https://raw.githubusercontent.com/ArtyETH06/artyeth06.github.io/main/ctf/lehack2025-wargame/stegafire/images/Pasted%20image%2020250630104103.png)


Really challenging — props and congrats to the other teams who pulled it off 💪🔥
Shoutout to Juliusxd23 and Bilal, my teammates with whom I solved the challenge!
