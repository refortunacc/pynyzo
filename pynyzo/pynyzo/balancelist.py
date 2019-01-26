

from pynyzo.messageobject import MessageObject
from pynyzo.helpers import base_app_log
from pynyzo.messagetype import MessageType
from pynyzo.fieldbytesize import FieldByteSize
import json
import struct


class BalanceList(MessageObject):
    """BalanceList message"""

    """
    __slots__ = ('_start_height', '_end_height', '_include_balance_list')

    def __init__(self, start_height: int=0, end_height: int=0, include_balance_list: bool=False,
                 buffer: bytes = None, app_log=None):
        # This replaces the various constructors from java, depending on the params
        super().__init__(app_log=app_log)
        if buffer:
            # buffer is the full buffer with timestamp and type, why the 10 offset.
            self._start_height = struct.unpack(">Q", buffer[10:10+8])[0]
            self._end_height = struct.unpack(">Q", buffer[10+8:10+8+8])[0]
            self._include_balance_list = struct.unpack("?", buffer[-1:])[0]
        else:
            self._start_height = start_height
            self._end_height = end_height
            self._include_balance_list = include_balance_list

    def get_start_height(self) -> int:
        return self._start_height

    def get_end_height(self) -> int:
        return self._end_height

    def include_balance_list(self) -> bool:
        return self._include_balance_list

    def get_byte_size(self) -> int:
        return FieldByteSize.blockHeight * 2 + FieldByteSize.booleanField

    def get_bytes(self) -> bytes:
        result = b''
        result += struct.pack(">Q", self._start_height)  # 8
        result += struct.pack(">Q", self._end_height)  # 8
        if self._include_balance_list:
            result += b'\x01'
        else:
            result += b'\x00'
        return result

    def to_string(self) -> str:
        return f"[BlockRequest({self._start_height}, {self._end_height}, {self._include_balance_list})]"

    def to_json(self) -> str:
        return json.dumps({"message_type": MessageType.BlockRequest11.name, 'value': {
            'start_height': self._start_height, 'end_height': self._end_height,
            'include_balance_list': self._include_balance_list}})
    """

    def print(self):
        """Create the status message and print it"""
        app_log = base_app_log()
        # app_log.info(self.to_string())
