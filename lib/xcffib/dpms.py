import xcffib
import struct
import six
MAJOR_VERSION = 0
MINOR_VERSION = 0
key = xcffib.ExtensionKey("DPMS")
_events = {}
_errors = {}
class GetVersionReply(xcffib.Reply):
    def __init__(self, unpacker):
        if isinstance(unpacker, xcffib.Protobj):
            unpacker = xcffib.MemoryUnpacker(unpacker.pack())
        xcffib.Reply.__init__(self, unpacker)
        base = unpacker.offset
        self.server_major_version, self.server_minor_version = unpacker.unpack("xx2x4xHH")
        self.bufsize = unpacker.offset - base
class GetVersionCookie(xcffib.Cookie):
    reply_type = GetVersionReply
class CapableReply(xcffib.Reply):
    def __init__(self, unpacker):
        if isinstance(unpacker, xcffib.Protobj):
            unpacker = xcffib.MemoryUnpacker(unpacker.pack())
        xcffib.Reply.__init__(self, unpacker)
        base = unpacker.offset
        self.capable, = unpacker.unpack("xx2x4xB23x")
        self.bufsize = unpacker.offset - base
class CapableCookie(xcffib.Cookie):
    reply_type = CapableReply
class GetTimeoutsReply(xcffib.Reply):
    def __init__(self, unpacker):
        if isinstance(unpacker, xcffib.Protobj):
            unpacker = xcffib.MemoryUnpacker(unpacker.pack())
        xcffib.Reply.__init__(self, unpacker)
        base = unpacker.offset
        self.standby_timeout, self.suspend_timeout, self.off_timeout = unpacker.unpack("xx2x4xHHH18x")
        self.bufsize = unpacker.offset - base
class GetTimeoutsCookie(xcffib.Cookie):
    reply_type = GetTimeoutsReply
class DPMSMode:
    On = 0
    Standby = 1
    Suspend = 2
    Off = 3
class InfoReply(xcffib.Reply):
    def __init__(self, unpacker):
        if isinstance(unpacker, xcffib.Protobj):
            unpacker = xcffib.MemoryUnpacker(unpacker.pack())
        xcffib.Reply.__init__(self, unpacker)
        base = unpacker.offset
        self.power_level, self.state = unpacker.unpack("xx2x4xHB21x")
        self.bufsize = unpacker.offset - base
class InfoCookie(xcffib.Cookie):
    reply_type = InfoReply
class dpmsExtension(xcffib.Extension):
    def GetVersion(self, client_major_version, client_minor_version, is_checked=True):
        buf = six.BytesIO()
        buf.write(struct.pack("=xx2xHH", client_major_version, client_minor_version))
        return self.send_request(0, buf, GetVersionCookie, is_checked=is_checked)
    def Capable(self, is_checked=True):
        buf = six.BytesIO()
        buf.write(struct.pack("=xx2x"))
        return self.send_request(1, buf, CapableCookie, is_checked=is_checked)
    def GetTimeouts(self, is_checked=True):
        buf = six.BytesIO()
        buf.write(struct.pack("=xx2x"))
        return self.send_request(2, buf, GetTimeoutsCookie, is_checked=is_checked)
    def SetTimeouts(self, standby_timeout, suspend_timeout, off_timeout, is_checked=False):
        buf = six.BytesIO()
        buf.write(struct.pack("=xx2xHHH", standby_timeout, suspend_timeout, off_timeout))
        return self.send_request(3, buf, is_checked=is_checked)
    def Enable(self, is_checked=False):
        buf = six.BytesIO()
        buf.write(struct.pack("=xx2x"))
        return self.send_request(4, buf, is_checked=is_checked)
    def Disable(self, is_checked=False):
        buf = six.BytesIO()
        buf.write(struct.pack("=xx2x"))
        return self.send_request(5, buf, is_checked=is_checked)
    def ForceLevel(self, power_level, is_checked=False):
        buf = six.BytesIO()
        buf.write(struct.pack("=xx2xH", power_level))
        return self.send_request(6, buf, is_checked=is_checked)
    def Info(self, is_checked=True):
        buf = six.BytesIO()
        buf.write(struct.pack("=xx2x"))
        return self.send_request(7, buf, InfoCookie, is_checked=is_checked)
xcffib._add_ext(key, dpmsExtension, _events, _errors)
