from .baseobject import BareObject
from .baseobject import PropertyType


class AdaptiveCard(BareObject):
    """
    Reference document for schema: https://adaptivecards.io/explorer/

    An Adaptive Card, containing a free-form body of card elements, and an optional set of actions.

    Property
    --------
    type : "AdaptiveCard"
        Must be "AdaptiveCard".	
    version : string
        Schema version that this card requires. If a client is lower than this version,
        the fallbackText will be rendered.
        NOTE: Version is not required for cards within an Action.ShowCard.
        However, it is required for the top-level card.
    refresh	: Refresh
        Defines how the card can be refreshed by making a request to the target Bot.
    authentication : Authentication
        Defines authentication information to enable on-behalf-of single sign on or just-in-time OAuth.
    body : Element[]
        The card elements to show in the primary card region.
    actions : Action[]
        The Actions to show in the card’s action bar.
    selectAction : ISelectAction
        An Action that will be invoked when the card is tapped or selected. Action.ShowCard is not supported.
    fallbackText : string
        Text shown when the client doesn’t support the version specified (may contain markdown).
    backgroundImage: BackgroundImage, uri
        Specifies the background image of the card.
    minHeight : string
        Specifies the minimum height of the card.
    speak : string
        Specifies what should be spoken for this entire card. This is simple text or SSML fragment.
    lang : string
        The 2-letter ISO-639-1 language used in the card. Used to localize any date/time functions.
    verticalContentAlignment :VerticalContentAlignment
        Defines how the content should be aligned vertically within the container.
        Only relevant for fixed-height cards, or cards with a minHeight specified.
    $schema : uri
        The Adaptive Card schema.
    """
    background_image = PropertyType(type=str, key_name='backgroundImage')
    vertical_content_alignment = PropertyType(type=str, key_name='verticalContentAlignment')
    select_action = PropertyType(type=str, key_name='selectAction')
    min_height = PropertyType(type=str, key_name='minHeight')
    fallback_text = PropertyType(type=str, key_name='fallbackText')
    body = PropertyType(type=list, key_name='body')
    actions = PropertyType(type=list, key_name='actions')
    speak = PropertyType(type=str, key_name='speak')
    lang = PropertyType(type=str, key_name='lang')

    def __init__(self) -> None:
        super().__init__()
        self.set_data('type', 'AdaptiveCard')
        self.set_data('version', '1.2')
        self.set_data('$schema', 'http://adaptivecards.io/schemas/adaptive-card.json')
