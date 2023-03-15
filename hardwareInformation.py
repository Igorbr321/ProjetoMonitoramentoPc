from typing import Optional
import re
import subprocess
import uuid
import socket
import platform
from gpiozero import CPUTemperature
import psutil
from gpuinfo import GPUInfo

def getCpuUsagePercentage():
    return psutil.cpu_percent()

def getGpuUsagePercentage():
    gpuUsagePercentage = str(GPUInfo.gpu_usage()[0])
    gpuUsagePercentage = gpuUsagePercentage.replace('[', '').replace(']', '')
    return gpuUsagePercentage

def getCpuModel():
    return platform.processor()

def getDesktop():
    return socket.gethostname()

def getMotherboardModel() -> Optional[uuid.UUID]:
    try:
        # Ask Windows for the device's permanent UUID. Throws if command missing/fails.
        txt = subprocess.check_output("wmic csproduct get uuid").decode()

        # Attempt to extract the UUID from the command's result.
        match = re.search(r"\bUUID\b[\s\r\n]+([^\s\r\n]+)", txt)
        if match is not None:
            txt = match.group(1)
            if txt is not None:
                # Remove the surrounding whitespace (newlines, space, etc)
                # and useless dashes etc, by only keeping hex (0-9 A-F) chars.
                txt = re.sub(r"[^0-9A-Fa-f]+", "", txt)

                # Ensure we have exactly 32 characters (16 bytes).
                if len(txt) == 32:
                    return uuid.UUID(txt)
    except:
        pass # Silence subprocess exception.

    return getMotherboardModel()