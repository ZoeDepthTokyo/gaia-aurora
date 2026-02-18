# Understandable — WCAG 2.1 Detailed Checks

## Form Labels (WCAG 3.3.2)
**Requirement**: Labels or instructions for inputs

```html
<!-- Good -->
<label for="email">Email Address</label>
<input id="email" type="email">

<!-- Bad -->
<input placeholder="Email">  <!-- Placeholder not a label -->
```

**Streamlit note**: Streamlit's `st.text_input("Label")` generates proper labels automatically. Avoid `label_visibility="hidden"` unless an alternative label is provided via ARIA.

## Manual Testing Guide

### Screen Reader Testing

**NVDA (Windows - Free)**
```
1. Install NVDA: https://www.nvaccess.org/
2. Start NVDA (Ctrl+Alt+N)
3. Navigate page:
   - H: Jump to headings
   - K: Jump to links
   - F: Jump to form fields
   - B: Jump to buttons
4. Listen: Is content understandable?
5. Check: Can you complete all tasks?
```

**VoiceOver (Mac - Built-in)**
```
1. Enable: System Settings → Accessibility → VoiceOver
2. Start: Cmd+F5
3. Navigate: VO+Right Arrow (VO = Ctrl+Option)
4. Interact: VO+Space
```

### Keyboard-Only Testing
```
1. Unplug mouse (literally)
2. Complete all tasks using only keyboard
3. Check:
   - Can you navigate entire UI?
   - Can you activate all buttons?
   - Can you fill all forms?
   - Can you close all modals?
4. Note any keyboard traps
```

### Color Blindness Testing
```
Tools:
- Chromium DevTools → Rendering → Emulate vision deficiencies
- Stark plugin (Figma)

Test:
- Protanopia (red-blind)
- Deuteranopia (green-blind)
- Tritanopia (blue-blind)
- Achromatopsia (monochrome)

Check: Is information still conveyed without color?
```
