# 8-Bit Animation System

## Core Rule

所有动画必须使用 steps() 时序函数 禁止 ease / linear / cubic-bezier 等平滑缓动
步数越少越有像素跳跃感 推荐 1-12 步

## Pixel Blink

```css
@keyframes pixelBlink {
  0%, 49% { opacity: 1; }
  50%, 100% { opacity: 0; }
}

.blink-fast {
  animation: pixelBlink 0.5s steps(1) infinite;
}

.blink-normal {
  animation: pixelBlink 1s steps(1) infinite;
}

.blink-slow {
  animation: pixelBlink 2s steps(1) infinite;
}
```

## Cursor Blink

```css
@keyframes cursorBlink {
  0%, 49% { border-right-color: var(--text-primary); }
  50%, 100% { border-right-color: transparent; }
}

.typing-cursor {
  border-right: 4px solid var(--text-primary);
  animation: cursorBlink 0.8s steps(1) infinite;
}
```

## Pixel Bounce (Staircase)

```css
@keyframes pixelBounce {
  0% { transform: translateY(0); }
  20% { transform: translateY(-12px); }
  40% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
  65% { transform: translateY(0); }
  75% { transform: translateY(-2px); }
  100% { transform: translateY(0); }
}

.bounce {
  animation: pixelBounce 0.8s steps(8) infinite;
}

.bounce-once {
  animation: pixelBounce 0.6s steps(6) forwards;
}
```

## Pixel Pop In

```css
@keyframes pixelPopIn {
  0% { transform: scale(0); opacity: 0; }
  50% { transform: scale(1.15); opacity: 1; }
  100% { transform: scale(1); opacity: 1; }
}

.pop-in {
  animation: pixelPopIn 0.3s steps(4) forwards;
}
```

## Pixel Shake (Hit Reaction)

```css
@keyframes pixelShake {
  0% { transform: translate(0, 0); }
  20% { transform: translate(-4px, 0); }
  40% { transform: translate(4px, 0); }
  60% { transform: translate(-4px, 0); }
  80% { transform: translate(4px, 0); }
  100% { transform: translate(0, 0); }
}

.shake {
  animation: pixelShake 0.3s steps(5) forwards;
}
```

## Damage Flash

```css
@keyframes damageFlash {
  0% { filter: brightness(1); }
  10% { filter: brightness(3); }
  20% { filter: brightness(1); }
  30% { filter: brightness(2.5); }
  40% { filter: brightness(1); }
  50% { filter: brightness(2); }
  60% { filter: brightness(1); }
  100% { filter: brightness(1); }
}

.damage {
  animation: damageFlash 0.6s steps(1) forwards;
}
```

## Typewriter Text

```css
@keyframes typewriter {
  from { width: 0; }
  to { width: 100%; }
}

.typewriter {
  overflow: hidden;
  white-space: nowrap;
  border-right: 4px solid var(--text-primary);
  animation:
    typewriter 2s steps(30) forwards,
    cursorBlink 0.8s steps(1) infinite;
}
```

## Scrolling Text (Marquee)

```css
@keyframes pixelScroll {
  0% { transform: translateX(100%); }
  100% { transform: translateX(-100%); }
}

.scroll-text {
  overflow: hidden;
  white-space: nowrap;
}

.scroll-text-inner {
  display: inline-block;
  animation: pixelScroll 8s steps(60) infinite;
}
```

## HP Bar Change

```css
@keyframes hpDecrease {
  0% { width: var(--hp-from); }
  100% { width: var(--hp-to); }
}

@keyframes hpFlash {
  0%, 30% { background: var(--status-danger); }
  15% { background: var(--text-primary); }
}

.hp-animate {
  animation: hpDecrease 0.8s steps(10) forwards;
}

.hp-critical {
  animation:
    hpDecrease 0.8s steps(10) forwards,
    hpFlash 0.4s steps(1) 3;
}
```

## EXP Bar Fill

```css
@keyframes expFill {
  0% { width: var(--exp-from); }
  100% { width: var(--exp-to); }
}

@keyframes expLevelUp {
  0% { width: var(--exp-from); }
  60% { width: 100%; }
  61% { width: 0%; }
  100% { width: var(--exp-to); }
}

.exp-animate {
  animation: expFill 1.2s steps(20) forwards;
}

.exp-levelup {
  animation: expLevelUp 1.5s steps(24) forwards;
}
```

## Level Up Effect

```css
@keyframes levelUpFlash {
  0%, 100% { box-shadow: none; }
  25% { box-shadow: 0 0 0 4px var(--accent-primary); }
  50% { box-shadow: 0 0 0 8px var(--accent-primary); }
  75% { box-shadow: 0 0 0 4px var(--accent-primary); }
}

@keyframes levelUpText {
  0% { transform: translateY(0); opacity: 1; }
  100% { transform: translateY(-32px); opacity: 0; }
}

.level-up-glow {
  animation: levelUpFlash 0.6s steps(4) 2;
}

.level-up-text {
  animation: levelUpText 1s steps(8) forwards;
}
```

## Pixel Fade In / Out

```css
@keyframes pixelFadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@keyframes pixelFadeOut {
  0% { opacity: 1; }
  100% { opacity: 0; }
}

.fade-in {
  animation: pixelFadeIn 0.4s steps(4) forwards;
}

.fade-out {
  animation: pixelFadeOut 0.4s steps(4) forwards;
}
```

## Pixel Slide

```css
@keyframes pixelSlideUp {
  0% { transform: translateY(16px); opacity: 0; }
  100% { transform: translateY(0); opacity: 1; }
}

@keyframes pixelSlideDown {
  0% { transform: translateY(-16px); opacity: 0; }
  100% { transform: translateY(0); opacity: 1; }
}

@keyframes pixelSlideLeft {
  0% { transform: translateX(16px); opacity: 0; }
  100% { transform: translateX(0); opacity: 1; }
}

@keyframes pixelSlideRight {
  0% { transform: translateX(-16px); opacity: 0; }
  100% { transform: translateX(0); opacity: 1; }
}

.slide-up { animation: pixelSlideUp 0.3s steps(4) forwards; }
.slide-down { animation: pixelSlideDown 0.3s steps(4) forwards; }
.slide-left { animation: pixelSlideLeft 0.3s steps(4) forwards; }
.slide-right { animation: pixelSlideRight 0.3s steps(4) forwards; }
```

## Selection Arrow (RPG Cursor)

```css
@keyframes arrowBounce {
  0%, 100% { transform: translateX(0); }
  50% { transform: translateX(4px); }
}

.select-arrow::before {
  content: "\25B6";
  display: inline-block;
  margin-right: 8px;
  animation: arrowBounce 0.6s steps(2) infinite;
}
```

## Star Twinkle

```css
@keyframes starTwinkle {
  0%, 40%, 100% { opacity: 1; }
  20% { opacity: 0; }
}

.star {
  position: fixed;
  width: 4px;
  height: 4px;
  background: var(--text-primary);
  pointer-events: none;
  z-index: -1;
}
```

## Stagger Delay Utilities

```css
.delay-1 { animation-delay: 0.1s; }
.delay-2 { animation-delay: 0.2s; }
.delay-3 { animation-delay: 0.3s; }
.delay-4 { animation-delay: 0.4s; }
.delay-5 { animation-delay: 0.5s; }
.delay-6 { animation-delay: 0.6s; }
.delay-7 { animation-delay: 0.7s; }
.delay-8 { animation-delay: 0.8s; }
```

## Constraints

- steps() 参数推荐范围: 1-12 超过 12 步像素感减弱
- transform 位移量必须是 4px 的整数倍
- 动画时长不低于 0.1s 不高于 3s (循环动画除外)
- 受击/伤害类动画使用 steps(1) 实现最硬的跳变
- 循环动画必须提供 animation-play-state 控制接口
- prefers-reduced-motion 媒体查询中应禁用所有动画
