import platform
import os


class Color:
    foreground_code = None
    background_code = None

    # TODO: accept color in rgb format
    def __init__(self, color_name, fg_code, bg_code='none', style=None):
        self.name = color_name
        self.foreground_code = fg_code

        self.background_code = None
        if bg_code == 'none':
            self.background_code = self.foreground_code + 10
        elif bg_code is None:
            self.background_code = None
        else:
            self.background_code = bg_code

        # style slector
        self.style = style
        self.style_code = 0
        self.style_code_selector()

        self._set_fg_and_bg_attribute()

    def style_code_selector(self, style=None):
        # TODO: make all style list in dictionary
        STYLE_TO_STYLE_CODE_MAPPER = {
            'bold': 1,
            'italic': 3,
            'underline': 4
        }
        if style in STYLE_TO_STYLE_CODE_MAPPER or self.style in STYLE_TO_STYLE_CODE_MAPPER:

            self.style_code = STYLE_TO_STYLE_CODE_MAPPER[style or self.style]

    def change_style(self, style):
        self.style_code_selector(style)
        self._set_fg_and_bg_attribute()

    def _set_fg_and_bg_attribute(self):
        self.fg = f"\033[{self.style_code};{self.foreground_code}m"
        self.fg_bg = f"\033[{self.style_code};{self.background_code};{self.foreground_code}m"
        self.bg = f"\033[{self.style_code};{self.background_code}m"

# source: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797


ANSI_COLOR_LIST = {
    'red': Color('red', 31, 41),
    'green':  Color('green', 32, 42),
    'yellow':  Color('yellow', 33, 43),
    'blue': Color('blue', 34, 44),
    'magenta': Color('magenta', 35, 45),
    'cyan': Color('cyan', 36, 36),
    'black': Color('black', 30, 40),

    'reset': Color('reset', 0, 0),
    'reset_color': Color('default', 39, 49),

    # aixterm specification
    'bright_black': Color('bright_black', 90),
    'bright_red': Color('bright_red', 91),
    'bright_green':  Color('bright_green', 92),
    'bright_yellow': Color('bright_yellow', 93),
    'bright_blue': Color('bright_blue', 94),
    'bright_cyan': Color('bright_cyan', 96),
    'bright_white': Color('bright_white', 97),
}

ANSI_COLOR_CODE = {
    'red': '\033[0;091m',
    'green': '\033[0;092m',
    'yellow': '\033[0;093m',
    'blue': '\033[0;034m',  # '\033[0;094m',
    'cyan': '\033[0;036m'

}


def print_colored(text, text_color, color_mode='auto', *args, **kwargs):
    platform_name = platform.platform()

    if color_mode in ('auto', 'always'):
        if platform_name.lower().startswith('Windows'):
            os.system('color')

        # if text_color in ANSI_COLOR_CODE:
        #     print(f"{ANSI_COLOR_CODE[text_color]}{text}\33[0m")
        if text_color in ANSI_COLOR_LIST:
            print(f"{ANSI_COLOR_LIST[text_color].fg}{text}{ANSI_COLOR_LIST['reset'].fg}")
        elif isinstance(text_color, Color):
            print(f"{text_color.fg}{text}{ANSI_COLOR_LIST['reset'].fg}")
        else:
            # if color not found, back to `old-fashioned` print
            print(f"{text}", *args, **kwargs)
    else:
        print(f"{text}", *args, **kwargs)


def colored_text(text, text_color, text_style=None, color_type='foreground') -> str:
    """
    This function return string that contain ANSI color value \
    that can be printed in terminal if the terminal support ANSI code value.

    @params text: text to color
    @params text_style: set output text style. Currently available option: \
                        'bold', 'italic', 'underline', None (default: None)
    @params color_type: set where the text will be colored. \
                        Current available option: \
                        'foreground', 'background' (default: 'foreground')
    """
    result_text_color = ''
    if text_color in ANSI_COLOR_LIST:
        color_object = ANSI_COLOR_LIST[text_color]
        color_object.change_style(text_style)

        if color_type == 'foreground':
            result_text_color = str(color_object.fg)
        elif color_type == 'background':
            result_text_color = str(color_object.bg)

        return f"{result_text_color}{text}{ANSI_COLOR_LIST['reset'].fg}"

    else:
        return text
