# Readme

#### Dependencies

1: Install nodes.js, refer: https://nodejs.org/en/download  <br>
2: git  <br>

`Note`: `npm`, which stands for `Node Package Manager`,

```
<!-- Install Yeoman and VS Code Extension Generator -->
$ npm install --global yo generator-code
```

#### my first extension

```
<!-- Draft TypeScript project -->
$ yo code

```

`Note:` <br>
`1:` update vscode version in file: `study_code_extension/myfirstextension/package.json` based on your current vscode version. <br>
    Need to remove:  <br>
    study_code_extension/myfirstextension/node_modules <br>
    study_code_extension/myfirstextension/package-lock.json <br>
    Run: `npm install` regenerate. <br>

`2:` F5 debug, create launch.json <br>
`3:` Ctrl+Shift+P, input `Hello World` to run. <br>
