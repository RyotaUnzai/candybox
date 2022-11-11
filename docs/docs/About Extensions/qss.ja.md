# QSSの拡張機能

## :root
:root は 擬似クラスで、グローバルの CSS 変数を宣言するのに便利です。
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
@import はアットルールで、他のスタイルシートからスタイルルールをインポートするために使用します。
```css
@import url("extra.qss");
```