from .baseobject import BareObject
from .baseobject import Element
from .baseobject import PropertyType


class TextBlock(Element):
    element_type = 'TextBlock'
    text = PropertyType(type=str, key_name='text')
    font_type = PropertyType(type=str, key_name='fontType')
    color = PropertyType(type=str, key_name='color')
    horizontalAlignment = PropertyType(type=str, key_name='horizontalAlignment')
    isSubtle = PropertyType(type=bool, key_name='isSubtle')
    maxLines = PropertyType(type=int, key_name='maxLines')
    size = PropertyType(type=str, key_name='size')
    weight = PropertyType(type=str, key_name='weight')
    wrap = PropertyType(type=bool, key_name='wrap')


class Image(Element):
    element_type = 'Image'
    url = PropertyType(type=str, key_name='url')
    altText = PropertyType(type=str, key_name='altText')
    backgroundColor = PropertyType(type=str, key_name='backgroundColor')
    height = PropertyType(type=str, key_name='height')
    horizontalAlignment = PropertyType(type=str, key_name='horizontalAlignment')
    selectAction = PropertyType(type=str, key_name='selectAction')
    size = PropertyType(type=str, key_name='size')
    style = PropertyType(type=str, key_name='style')
    width = PropertyType(type=str, key_name='width')


# TODO: Correct type for sources as array of MediaSource
class Media(Element):
    element_type = 'Media'
    sources = PropertyType(type=list, key_name='sources')
    poster = PropertyType(type=str, key_name='poster')
    altText = PropertyType(type=str, key_name='altText')


class MediaSource(BareObject):
    mimeType = PropertyType('mimeType')
    url = PropertyType(type=str, key_name='url')


"""
Example for RichTextBlock:
{
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "type": "AdaptiveCard",
  "version": "1.2",
  "body": [
    {
      "type": "RichTextBlock",
      "inlines": [
        "This is the first inline. ",
        {
          "type": "TextRun",
          "text": "We support colors,",
          "color": "good"
        },
        {
          "type": "TextRun",
          "text": " both regular and subtle. ",
          "isSubtle": true
        },
        {
          "type": "TextRun",
          "text": "Text ",
          "size": "small"
        },
        {
          "type": "TextRun",
          "text": "of ",
          "size": "medium"
        },
        {
          "type": "TextRun",
          "text": "all ",
          "size": "large"
        },
        {
          "type": "TextRun",
          "text": "sizes! ",
          "size": "extraLarge"
        },
        {
          "type": "TextRun",
          "text": "Light weight text. ",
          "weight": "lighter"
        },
        {
          "type": "TextRun",
          "text": "Bold weight text. ",
          "weight": "bolder"
        },
        {
          "type": "TextRun",
          "text": "Highlights. ",
          "highlight": true
        },
        {
          "type": "TextRun",
          "text": "Italics. ",
          "italic": true
        },
        {
          "type": "TextRun",
          "text": "Strikethrough. ",
          "strikethrough": true
        },
        {
          "type": "TextRun",
          "text": "Monospace too!",
          "fontType": "monospace"
        }
      ]
    },
    {
      "type": "RichTextBlock",
      "inlines": [
        {
          "type": "TextRun",
          "text": "Date-Time parsing: {{DATE(2017-02-14T06:08:39Z,LONG)}} {{TIME(2017-02-14T06:08:39Z)}}"
        }
      ]
    },
    {
      "type": "RichTextBlock",
      "horizontalAlignment": "center",
      "inlines": [
        {
          "type": "TextRun",
          "text": "Rich text blocks also support center alignment. Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor "
        }
      ]
    },
    {
      "type": "RichTextBlock",
      "horizontalAlignment": "right",
      "inlines": [
        {
          "type": "TextRun",
          "text": "Rich text blocks also support right alignment. Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor "
        }
      ]
    },
    {
      "type": "RichTextBlock",
      "inlines": []
    }
  ]
}
"""


class RichTextBlock(Element):
    element_type = 'RichTextBlock'
    url = PropertyType(type=str, key_name='url')
    inlines = PropertyType(type=list, key_name='inlines')
    horizontalAlignment = PropertyType(type=str, key_name='horizontalAlignment')


class TextRun(Element):
    element_type = 'TextRun'
    text = PropertyType(type=str, key_name='text')
    color = PropertyType(type=str, key_name='color')
    fontType = PropertyType(type=str, key_name='fontType')
    highlight = PropertyType(type=bool, key_name='highlight')
    isSubtle = PropertyType(type=bool, key_name='isSubtle')
    italic = PropertyType(type=bool, key_name='italic')
    selectAction = PropertyType(type=str, key_name='selectAction')
    size = PropertyType(type=str, key_name='size')
    strikethrough = PropertyType(type=bool, key_name='strikethrough')
    underline = PropertyType(type=bool, key_name='underline')
    weight = PropertyType(type=str, key_name='weight')
