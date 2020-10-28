# **EasyTk** 

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

#### Usage

##### JSON strucuture:

```json
{
...,
  "Frame1": {
    "layout": "grid",
    "methods": [0,1,2],
    "master": "FrameContainer",
    "config": {},
    "grid": {"sticky": "NSEW"},
    "newRow": false
  },...
}
```
You stat with name of widget,for example:
``Frame1:{...},"LabelUsername":{...},"ButtonConfirm":{...},...``

**layout** - currently you can use grid and pack
``"layout":"grid"`` or ``"layout:"pack"``

**methods** - inside this list you can include indexes of methods that you will use,this is explained in Python part

**master** - to which master does this widget belong,be aware of which layout manager is used and that master exists

**config** - for example: ``"config":{"text":"TEST"}``

**grid** - if you decided to use grid as layout then fill this with proper data,you don't have to include row and column,for example:
``"Button1":{...},Button2":{...},Button3":{..., "newRow":true },``

Button1 is on row=0,column=0,Button2 is on row=0,column=1 and Button3 is on _row=1_,column=0.
But you can also include row and column if you want.

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
This class has all methods you need for "converting" JSON to Tkinter app.EasyTkObject mainly use EasyTk methods but in different way.
You can override them.

* ``create_root()``
* ``get(name,obj=True)``- getting object of one widget if ``obj`` were ``False`` then you will get EasyTkChild object
* ``import_methods(methods=[])`` - put all your methods in list and use this method
* ``import_modules(modules=[])`` - put all your modules here,you can include your own widgets,default is this ``["Frame","Entry","Button","Label","Separator","Radiobutton","Canvas","Scrollbar"]``,you can extend it
* ``open_file(file)`` - setting your json file EasyTk
* ``reading_from_json()`` - adding every widget to screen
*  ``add_just_one(file,key)`` - adding just one widget from json(again be sure that master there exist)
* ``easy_factory()`` - factory for EasyTk object
