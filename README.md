st2-WPStyle
===========

This plugin works to modify code to the WordPress style.

## Directory

    ├Sublime Text 2
        ├─Packages
            ├─WPStyle
                ├── Default\ (Linux).sublime-keymap
                ├── Default\ (OSX).sublime-keymap
                ├── Default\ (Windows).sublime-keymap
                ├── WPStyle.py
                └── README.md

## How to use

1. The clone in the package folder

        $ cd /path/to/Sublime Text 2/Packages
        $ git clone https://github.com/yuka2py/WPStyle.git

2. Execution from the Command Palette.

        WPStyle: Apply style to selection or all

    Applied to the selection.
    If not selected regions, apply to whole of the current file.


## Sample

    if (have_posts()) while (have_posts()) the_post();

changes after...

    if ( have_posts() ) while ( have_posts() ) the_post();

