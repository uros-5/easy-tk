# **EasyTk** 

[![Downloads](https://pepy.tech/badge/easy-tk)](https://pepy.tech/project/easy-tk)

Create Tkinter applications with help of JSON!

```python
test = EasyTkObject()
test.create_root()
test.open_file("json/test.json")
test.reading_from_json()
test.start_root()
```

### Installation

If you don't have tkinter installed in your environment,install it:
```python
pip install tkintertable
```
then install this package.

```
pip install easy-tk
```

#### Usage

##### JSON strucuture:

```json
{
...,
  "Frame1": {
    "layout": "grid",
    "methods": ["confirm_click","add_click","set.."],
    "master": "FrameContainer",
    "config": {"config_key":"config_value","config_key":"var:something"},
    "grid": {"sticky": "NSEW"},
    "newRow": false
  },...
}
```
You start with name of widget,for example:
``Frame1:{...},"LabelUsername":{...},"ButtonConfirm":{...},...``

**layout** - you can use grid or pack or place
``"layout":"grid"`` or ``"layout:"pack"``

**methods** - inside this list you can include names of methods that you will use,this is explained in Python part

**master** - to which master does this widget belong,be aware of which layout manager is used and that master exists

**config** - for example: ``"config":{"text":"TEST"}`` or if you imported your variables then just call ```"config":{"some_key":"var:something"}```

**grid** - if you decided to use grid as layout then fill this with proper data,you don't have to include row and column,for example:
``"Button1":{...},Button2":{...},Button3":{..., "newRow":true },``

Button1 is on ```row=0,column=0```,Button2 is on ```row=0,column=1``` and Button3 is on ```_row=1_,column=0```.
But you can also include row and column if you want. With that in mind,next column is from place where you /didn't/ specified column.

**pack** - if layout is pack then include here attributes,or leave it blank.

If you use pack then it's necessary to include it in JSON object even if you don't have any value.
For example:
```json
...,
"Canvas": {
    "master": "Frame0",
    "layout": "pack",
    "pack": {"side":"left", "fill":"both", "expand":true},
    "config": {},
    "methods": [1]
  },
"Scrollbar": {
    "master": "Frame0",
    "layout": "pack",
    "pack": {},
    "config": {"orient": "vertical"},
    "methods": [2]
},
...
```
Both widgets work. And same applies to grid.

**newRow** - if layout is grid then use boolean value.

##### Python

```python
from easy_tk import EasyTkObject
```
This class has all methods you need for "converting" JSON to Tkinter app. EasyTkObject mainly use EasyTk methods but in different way.
You can override them.

* ``create_root()``
* ``get(name,obj=True)``- getting object of one widget if ``obj`` were ``False`` then you will get EasyTkChild object
* ``import_methods(methods={})`` - put all your methods in dict and then just call that method in json list. ```...,"methods":["on_check_btn","set_style_btns","exit_app",...]```
* ``import_modules(modules={})`` - put all your modules here,you can include your own widgets,default is this ``["Frame","Entry","Button","Label","Separator","Radiobutton","Canvas","Scrollbar"]``,you can extend it
* ```import_variables(variables={})``` - include only variables that you need for config,call them with ```"var:some_key"```
* ``open_file(file)`` - setting your json file EasyTk
* ``reading_from_json()`` - adding every widget to screen,applying all config values,calling all methods you included
*  ``add_just_one(file,key)`` - adding just one widget from json(again be sure that master there exist),for example ```add_just_one("json/test.json","Canvas5")```
* ``easy_factory()`` - factory for EasyTk object


##### Other info

On [github](https://github.com/uros-5/easy-tk) you can find helpers folder,there is shortcut for adding scrollbar in your entire window. In future I will add more of them that you can use.

##### Examples of usage

[football-video-editor-python](https://github.com/uros-5/football-video-editor-python)

##### Changes

1.0.7.1 added support for older version in creating master

1.0.6.4 added methods for removing widgets and for changing keys in json before displaying widgets on screen

1.0.6.3 fixed modules error while loading one widget

1.0.6.2 - fixed using variables inside json for grid/pack

1.0.6 - you don't have to specify all_widgets parameter in your methods that are connected with json

