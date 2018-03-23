# awselect_sublime_plugin
Extract the text between matching words to new file

## Usage:
1. Select the word and press <kbd>Ctrl</kbd> + <kbd>d</kbd> to select the two matching words. 
2. Now press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>x</kbd> or right click and select `Awselecttofile` option.
3. This will extract the text between matching words to new file.

## Example:
```
this is line one
test_extract
this is line two
this is line three
test_extract
this is line four
```

If I select both test_extract using <kbd>Ctrl</kbd> + <kbd>d</kbd> and then press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>x</kbd>, it will output following text in new file.

```
test_extract
this is line two
this is line three
test_extract
```

## Installation:

### Manual Install (*Recommended*)

1. Click the `Preferences > Browse Packages…` menu
2. Browse up a folder and then into the `Installed Packages/` folder
3. Download [Awselecttofile.sublime-package](https://github.com/ashwinwadte/awselect_sublime_plugin/raw/master/Awselecttofile.sublime-package) and copy it into the `Installed Packages/` directory
4. Restart Sublime Text


### Using Package Control (*Support is not added yet*)

1. If Package Control is not installed, in Sublime Text, go to `Tools -> Install Package Controll...`

![Install Package Control](img/install_package_control.PNG)


2. Open Package Control - `Preferences -> Package Control`

![Package Control](img/package_control.png)


3. Select `Package Control: Add Repository`

![Add Repository](img/add_repository.png)


4. At the bottom of the Sublime window, a input will appear, copy and paste the URL: `https://github.com/ashwinwadte/awselect_sublime_plugin` 

![Copy Repository](img/copy_repository.png)


5. Open Package Control again - Preferences -> Package Control

![Package Control](img/package_control.png)


6. Select `Package Control: Install Packages`

![Install Package](img/install_package.png)


7. Now if you right click, you can see `Awselecttofile` option added to your context menu.
