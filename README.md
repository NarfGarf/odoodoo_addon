# Como agregar un modulo nuevo a Odoo
## Paso 1:
Tener la estructura correcta (no es necesario tenerlo en github)
```
<custom_module>
  __init__.py
  __manifest__.py
  <models>
    __init__.py
    my_module.py
  </models>
  <views>
    my_model_views.xml
  </views>
  <security>
    ir.model.access.csv
  </security>
</custom_module>
```
Meter en `__init__.py`
```
from . import models
```
Meter en `__manifest__.py`
```
{
 'name': 'My Custom Module',
 'version': '1.0',
 'summary': 'Simple module to demonstrate Odoo development',
 'author': 'Your Name',
 'depends': ['base'],
 'data': [
     'security/ir.model.access.csv',
     'views/my_model_views.xml',
 ],
 'installable': True,
 'application': True,
}
```
Meter en `models/__init__.py`
```
from . import my_model


file: models/my_model.py

from odoo import models, fields

class MyModel(models.Model):
 _name = 'my.model'
 _description = 'My Custom Model'

 name = fields.Char(string='Name', required=True)
 description = fields.Text(string='Description')
```
Meter en `views/my_model_views.xml`
```
<odoo>
 <!-- Form View -->
 <record id="view_form_my_model" model="ir.ui.view">
     <field name="name">my.model.form</field>
     <field name="model">my.model</field>
     <field name="arch" type="xml">
         <form string="My Model">
             <sheet>
                 <group>
                     <field name="name"/>
                     <field name="description"/>
                 </group>
             </sheet>
         </form>
     </field>
 </record>

 <!-- List View -->
 <record id="view_tree_my_model" model="ir.ui.view">
     <field name="name">my.model.list</field>
     <field name="model">my.model</field>
     <field name="arch" type="xml">
         <list>
             <field name="name"/>
         </list>
     </field>
 </record>

 <!-- Action -->
 <record id="action_my_model" model="ir.actions.act_window">
     <field name="name">My Models</field>
     <field name="res_model">my.model</field>
     <field name="view_mode">list,form</field>
 </record>

 <!-- Menu -->
 <menuitem id="menu_my_custom_module_root" name="My Module"/>
 <menuitem id="menu_my_model" name="My Models" parent="menu_my_custom_module_root" action="action_my_model"/>
</odoo>
```
Meter en `security/ir.model.access.csv`
```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_my_model_user,access_my_model_user,model_my_model,,1,1,1,1
```
## Paso 2:
Ir a la carpeta custom_addons de tu Odoo y agregar tu carpeta custom_module adentro
## Paso 3:
Prender / Reiniciar tu Odoo
## Paso 4:
Ir a Settings y activar modo desarrollador

<img width="670" height="668" alt="image" src="https://github.com/user-attachments/assets/fb130dba-96a8-4936-9807-7305bbf32b0d" />

## Paso 5:
Ir a Apps y hacer click en "Update Apps List", elegir tu modulo y hacer click en Install

<img width="827" height="420" alt="image" src="https://github.com/user-attachments/assets/61aea083-2c31-46aa-8c68-f1d73efd322e" />

### Warning
Esto no se puede hacer en la version gratuita de Render
