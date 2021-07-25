from .baseobject import BareObject
from .baseobject import Element
from .baseobject import PropertyType


class Container(Element):
    """
        "type": {
          "enum": [
            "Container"
          ],
          "description": "Must be `Container`"
        },
        "items": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/ImplementationsOf.Element"
          },
          "description": "The card elements to render inside the `Container`."
        },
        "selectAction": {
          "$ref": "#/definitions/ImplementationsOf.ISelectAction",
          "description": "An Action that will be invoked when the `Container` is tapped or selected. `Action.ShowCard` is not supported.",
          "version": "1.1"
        },
        "style": {
          "anyOf": [
            {
              "$ref": "#/definitions/ContainerStyle"
            },
            {
              "type": "null"
            }
          ],
          "description": "Style hint for `Container`."
        },
        "verticalContentAlignment": {
          "$ref": "#/definitions/VerticalContentAlignment",
          "description": "Defines how the content should be aligned vertically within the container.",
          "default": "top",
          "version": "1.1"
        },
        "bleed": {
          "type": "boolean",
          "description": "Determines whether the element should bleed through its parent's padding.",
          "version": "1.2",
          "features": [
            2109
          ]
        },
        "backgroundImage": {
          "anyOf": [
            {
              "$ref": "#/definitions/BackgroundImage"
            },
            {
              "type": "string",
              "format": "uri-reference",
              "description": "The URL (or data url) to use as the background image. Supports data URI."
            }
          ],
          "description": "Specifies the background image. Acceptable formats are PNG, JPEG, and GIF",
          "version": "1.2"
        },
        "minHeight": {
          "type": "string",
          "description": "Specifies the minimum height of the container in pixels, like `\"80px\"`.",
          "examples": [
            "50px"
          ],
          "version": "1.2",
          "features": [
            2293
          ]
        },
        "fallback": {},
        "height": {},
        "separator": {},
        "spacing": {},
        "id": {},
        "isVisible": {},
        "requires": {}
    """

    element_type = 'Container'
    bleed = PropertyType(type=bool)
    min_height = PropertyType(type=str, key_name='minHeight')
    background_image = PropertyType(type=str, key_name='backgroundImage')
    vertical_content_alignment = PropertyType(type=str, key_name='verticalContentAlignment')
    style = PropertyType(type=str)
    select_action = PropertyType(type=str, key_name='selectAction')
    items = PropertyType(type=list)


# TODO: Correct `actions` as array of Action
class ActionSet(Element):
    element_type = 'ActionSet'
    actions = PropertyType(type=list)


# TODO: Correct `columns` as array of Column
class ColumnSet(Element):
    element_type = 'ColumnSet'
    columns = PropertyType(type=list)
    select_action = PropertyType(type=str, key_name='selectAction')
    style = PropertyType(type=str)
    bleed = PropertyType(type=bool)
    min_height = PropertyType(type=str, key_name='minHeight')
    horizontal_alignment = PropertyType(type=str, key_name='horizontalAlignment')


class Column(Element):
    element_type = 'Column'
    items = PropertyType(type=list, key_name='items')
    backgroundImage = PropertyType(type=str, key_name='backgroundImage')
    bleed = PropertyType(type=bool, key_name='bleed')
    minHeight = PropertyType(type=str, key_name='minHeight')
    horizontalAlignment = PropertyType(type=str, key_name='horizontalAlignment')
    separator = PropertyType(type=bool, key_name='separator')
    selectAction = PropertyType(type=str, key_name='selectAction')
    style = PropertyType(type=str, key_name='style')
    verticalContentAlignment = PropertyType(type=str, key_name='verticalContentAlignment')
    width = PropertyType(type=str, key_name='width')


class FactSet(Element):
    element_type = 'FactSet'
    facts = PropertyType(type=list, key_name='facts')


class Fact(BareObject):
    title = PropertyType(type=str)
    value = PropertyType(type=str)


# TODO: Correct `images` as array of Image
class ImageSet(Element):
    element_type = 'ImageSet'
    images = PropertyType(type=list)
    image_size = PropertyType(type=str, key_name='imageSize')
