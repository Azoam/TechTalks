Modal Typing:
1. Insert: Allows you to type
2. Visual: Allows you to highlight (usually for deleting)
3. Visual Block: Allows you to highlight a rectangular block of text
4. Replace: Allows you to type over text
5. Normal: Root mode


Inserting:
1. Enter insert Mode: `i`
2. Move over a character and enter insert mode: `a`
3. Delete currently selected character and enter insert mode: `s`
4. Jump to end of line in insert mode: `A`
5. Jump to beginning of line in insert mode: `I`
6. Create a new line one line below, move to down to new line and enter insert mode: `o`
7. Create a new line one line up, move up to new line and enter insert mode: `O`


Normal:
1. By Default, you start in normal mode
2. Get back to normal mode: `esc`


Visual Mode:
1. To start highlighting: `v`
2. Use arrow keys (or home row) to highlight more characters
3. Delete highlighted text: `d`
4. To paste just deleted text: `p`
5. Use mouse to move cursor and highlight: `:set mouse=a`


Replace Mode:
1. Enter replace mode: `r`
2. Type to overwrite text


Writing and Quitting:
1. Save: `:w`
2. Quit file: `:q`
3. Quit unsaved file: `:q!`
4. Shortcut to save and quit: `:wq`


Movement:
1. Arrow Keys: up, down, left right
2. Home Row:
   - Move left:    `h`
   - Move Up:      `j`
   - Move Down:    `k`
   - Move Right:   `l`
3. Go to top of file: `gg`
4. Go to bottom of file: `G`
5. Go to specific line number: `:<line number>, followed by enter when you're done
   - EX: `: 122` - Goes to line 122
6. Scroll down by screen length: `ctrl + d`


Advanced Navigation:
1. Move to beginning of Line: `0`
2. move to end of line: `$`
3. Move to next word: `w`
4. Move back one word: `W`
5. Move to last character in word: `e`
6. Move forward to next instance of said character:
   - EX: `fG` - going forward, move the next instance of the letter `G`
7. Move backwards to previous instance of said character:
    - EX: `FG` - going backwards, move the previous instance of the letter `G`


Delete:
1. Delete Line: `dd`
2. Delete x number of lines: `xdd`
   - EX: `5dd` deletes 5 lines
3. Delete character being hover over: `x`
4. Delete word going forward: `dw`
5. Delete word going backwards: `db`
6. Delete inside brace term: `di(`, `di{`, `di[`, etc (closing tag also works)
    - Ex: If I want to delete what's inside the quotations for the following term:
          1.) Move cursor to be inside the string
          2.) Type: `di"`
    - EX: System.out.println("Hello | world!");
          (`|` character is the cursor in this example), `di"`
          returns System.out.println("");


Undo/Redo
1. Undo previous action: `u`
2. Redo previous action: `ctrl + r`


Copy/Cut & Paste:
1. Copy current line: `yy`
2. Copy # number of lines: `#yy`
   - EX: `5yy` copies current line and 4 below
3. Deleting in vim is cutting
4. Paste: `p`


Search:
1. Start searching: `/<search term>` then press enter when you're done
   -EX: To search `banana` you type: `/banana`
2. To find next instance of word: `n`
3. To find previous instance of word: `N`
4. You can search using regex
5. Different Types of searches:
    - highlights the terms as you search: `:set incrsearch`
    - highlights terms when you're done searching: `:set hlsearch` (default search)


Terminal/Shell
1. Run terminal command without leaving vim: `! <command>`
2. Run terminal command and write output to vim: `read ! <command>`
   - EX: `read ! ls` - writes all files and folders in current directory into file
   - Shortcut: :r! <command>
3. Open terminal without leaving vim session: `:shell`
    - Shortcut is: `:sh`


Visual Block Mode:
1. Enter visual block mode: `ctrl + v`
2. Use Arrow keys (or home row) to highlight block
3. While in visual block mode, `I` well let you insert text in beginning of said column


Revert File:
1. Revert File back to previous state: `:earlier #m`
    - EX `:earlier 15m` reverts back 15 minutes
    - Facts: Also works with seconds, hours, and days


Split Screens:
1. Split screen horizontally: `:split <file-path>`
2. Split screen vertically: `:vsplit <file-path>`
3. To switch windows: `ctrl + w, direction`


Spell Check:
1. Turn on spell check for English `:setlocal spell spelllang=en_us`
2. See suggestions to correct word: `z=`


vimrc: Used to customize Vim settings when you open it
1. create vimrc in home directory by typing `touch .vimrc`
2. [link to basic .vimrc]
