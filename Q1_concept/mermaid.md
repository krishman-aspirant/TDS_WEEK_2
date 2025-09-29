
```mermaid
---
title: Node
---
flowchart LR
    id
```
# setup
1. Install a VS Code extension
1. Go to Extensions (Ctrl+Shift+X)

1. Search for “Markdown Preview Mermaid Support” (by Matt Bierner) or “Markdown Preview Enhanced”

1. Install it.

> "  ```mermaid  "  -> at starting of mermaid code write this

> Then , title under three ---

> flowchart LR(left to right)  then below it something that you want to write in BOX


## Example
```mermaid
---
title: My Title
---
flowchart TB
    Something
```
### E2
```mermaid
flowchart LR
    id["This ❤ Unicode"]
```

### E3

```mermaid

flowchart LR
    markdown["`This **is** _Markdown_`"]
    newLines["`Line1
    Line 2
    Line 3`"]
    markdown --> newLines
```

### E4
```mermaid
flowchart TD
    Start --> Stop
```

### E5
```mermaid
flowchart LR
    markdown[Mai **Pagal** ho raha hun]--> NO

```

### E6
```mermaid
flowchart LR
    id1(This is the text in the box)

```




### E7
```mermaid
flowchart TD

    id1(((This is the text in the circle)))


```

> There are many more diagram to learn in mermaid.

### E8
```mermaid
flowchart LR
    A-- This is the text! -----B

```

### E9
```mermaid
flowchart LR
   a --> b & c--> d

```

### E10
```mermaid
flowchart LR
  A e1@==> B
  e1@{ animate: true }
```

### E11
```mermaid
flowchart TB
    c1-->a2

    subgraph one
    a1-->a2
    end

    subgraph two
    b1-->b2
    end

    subgraph three
    c1-->c2
    end
```

### E12
```mermaid
flowchart LR
    A-->B
    B-->C
    C-->D
    click A callback "Tooltip for a callback"
    click B "https://www.github.com" "This is a tooltip for a link"
    click C call callback() "Tooltip for a callback"
    click D href "https://www.github.com" "This is a tooltip for a link"

```