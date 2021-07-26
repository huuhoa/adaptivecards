import enum


class SpacingType(str, enum.Enum):
    """
      Specifies how much spacing. Hosts pick the exact pixel amounts for each of these.
    """
    DEFAULT = 'default'
    NONE = "none",
    SMALL = "small",
    MEDIUM = "medium",
    LARGE = "large",
    EXTRA_LARGE = "extraLarge",
    PADDING = "padding"


class ColorType(str, enum.Enum):
    DEFAULT = "default"
    DARK = "dark"
    LIGHT = "light"
    ACCENT = "accent"
    GOOD = "good"
    WARNING = "warning"
    ATTENTION = "attention"


class ContainerStyleType(str, enum.Enum):
    DEFAULT = "default"
    EMPHASIS = "emphasis"
    GOOD = "good"
    ATTENTION = "attention"
    WARNING = "warning"
    ACCENT = "accent"


class FontSize(str, enum.Enum):
    DEFAULT = "default"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extraLarge"


class FontWeight(str, enum.Enum):
    DEFAULT = "default"
    LIGHTER = "lighter"
    BOLDER = "bolder"


class HorizontalAlignment(str, enum.Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class VerticalAlignment(str, enum.Enum):
    TOP = "top"
    CENTER = "center"
    BOTTOM = "bottom"


class VerticalContentAlignment(str, enum.Enum):
    TOP = "top"
    CENTER = "center"
    BOTTOM = "bottom"


class ImageSize(str, enum.Enum):
    """
    Controls the approximate size of the image.
    The physical dimensions will vary per host.
    Every option preserves aspect ratio.
    """
    AUTO = "auto"
    STRETCH = "stretch"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class ImageStyle(str, enum.Enum):
    """
    Controls how this `Image` is displayed.
    """
    DEFAULT = "default"
    PERSON = "person"
