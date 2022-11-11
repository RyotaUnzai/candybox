# QSS Extensions

## :root
:root is a pseudo-class, useful for declaring global CSS variables.
```css
:root {
    --background-color1: #2c2b30;
    --main-color1: hotpink;
}

QMainWindow {
    background-color: var(--background-color1);
    color: var(--main-color1);
}
```


## @import
@import is an at-rule, used to import style rules from other style sheets.
```css
@import url("extra.qss");
```