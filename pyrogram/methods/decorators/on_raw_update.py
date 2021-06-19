#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import Any, Callable

import pyrogram
from pyrogram.scaffold import Scaffold

Func = Callable[[pyrogram.Client,
                 pyrogram.types.Update, Any, Any], Any]
Decorator = Callable[[Func], Func]


class OnRawUpdate(Scaffold):
    def on_raw_update(
        self=None,
        group: int = 0
    ) -> Decorator:
        """Decorator for handling raw updates.

        This does the same thing as :meth:`~pyrogram.Client.add_handler` using the
        :obj:`~pyrogram.handlers.RawUpdateHandler`.

        Parameters:
            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Func) -> Func:
            if isinstance(self, pyrogram.Client):
                self.add_handler(pyrogram.handlers.RawUpdateHandler(func), group)
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(
                    (
                        pyrogram.handlers.RawUpdateHandler(func),
                        group if self is None else group
                    )
                )

            return func

        return decorator
