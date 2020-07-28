# shamelessly lifted from https://makina-corpus.com/blog/metier/2016/the-worlds-simplest-python-template-engine

import string


class SuperFormatter(string.Formatter):
    """World's simplest Template engine."""

    def format_field(self, value, spec):
        if spec.startswith('repeat'):
            template = spec.partition(':')[-1]
            if type(value) is dict:
                value = value.items()
            yo = ''.join([self.format(template, item=item) for item in value])
            # print(f"yoyoyo: {yo}")
            return yo
        elif spec == 'call':
            return value()
        elif spec.startswith('if'):
            return (value and spec.partition(':')[-1]) or ''
        else:
            return super(SuperFormatter, self).format_field(value, spec)


# class SuperFormatter(string.Formatter):
#     """World's simplest Template engine."""
#
#     def format_field(self, value, spec):
#         cwe = None
#         mitigations = None
#         if spec.startswith('repeat'):
#             template = spec.partition(':')[-1]
#             if type(value) is dict:
#                 # value = value.items()
#                 for k, v in value.items():
#                     if type(v) is dict:
#                         for k_, v_ in v.items():
#                             if type(v_) is dict:
#                                 v_ = value.items()
#                                 mitigations = ''.join([self.format(template, item=item) for item in v_])
#                                 v[k_] = mitigations
#
#                         v = value.items()
#                         cwe = ''.join([self.format(template, item=item) for item in v])
#
#             return ''.join([self.format(template, item=item) for item in value])
#         elif spec == 'call':
#             return value()
#         elif spec.startswith('if'):
#             return (value and spec.partition(':')[-1]) or ''
#         else:
#             return super(SuperFormatter, self).format_field(value, spec)
