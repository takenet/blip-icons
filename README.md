# BLiP Visual Assets Catalog

Base project for BLiP's SVG and PNG catalog, that can expand to other assets if necessary.

hmg-design.blip.ai

## Creating an icon library

To create an album library, you must run a python command to run through all files in an "all" directory with "icon", "logo" and "illustration" directory.

Look into the folder src > assets > img > organized-new. There is a pattern of Project > all > icon/logo/illustration. It is important to have a copy of the files create-defs.py, file-cleaner.py and svg-creator.py in the Project folder.
Add the SVG files downloaded from Figma to each of the corresponding folders: icons for symbols that have 72x72 px; logos for branding images; illustration for generalistic arts.

Then, run this command in the Project folder's path:

```
python create-defs.py
```

CreateDefs will call FileCleaner to clean SVG files from unecessary code, such as some "fill=none" or "fill=black" on icon files. If you would like to use a SVG file alone (without libraries) or inline SVGs, you can get your cleaned file from the "clean" directory after running the code. Then, it calls SVGCreator to create the SVG library, which can be used with the USE tag in svgs.

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production

It is important to build before pushing changes, so the website can be updated.

```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
