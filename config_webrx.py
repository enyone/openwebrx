# -*- coding: utf-8 -*- 

"""
config_webrx: configuration options for OpenWebRX

	This file is part of OpenWebRX, 
	an open-source SDR receiver software with a web UI.
	Copyright (c) 2013-2015 by Andras Retzler <randras@sdr.hu>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	In addition, as a special exception, the copyright holders
	state that config_rtl.py and config_webrx.py are not part of the 
	Corresponding Source defined in GNU AGPL version 3 section 1. 
	
	(It means that you do not have to redistribute config_rtl.py and 
	config_webrx.py if you make any changes to these two configuration files,
	and use them for running your web service with OpenWebRX.)
"""
# ==== Server settings ====
web_port=8073
server_hostname="localhost" # If this contains an incorrect value, the web UI may freeze on load (it can't open websocket)
max_clients=20

# ==== Web GUI configuration ====
receiver_name="[Callsign]"
receiver_location="Budapest, Hungary"
receiver_qra="JN97ML"
receiver_asl=200
receiver_ant="Longwire"
receiver_device="RTL-SDR"
receiver_admin="example@example.com"
receiver_gps=(47.000000,19.000000)
photo_height=350
photo_title="Panorama of Budapest from Schönherz Zoltán Dormitory"
photo_desc="""
You can add your own background photo and receiver information.<br />
Receiver is operated by: <a href="mailto:%[RX_ADMIN]">%[RX_ADMIN]</a><br/>
Device: %[RX_DEVICE]<br />
Antenna: %[RX_ANT]<br />
Website: <a href="http://localhost" target="_blank">http://localhost</a>
"""

# ==== sdr.hu listing ====
# If you want your ham receiver to be listed publicly on sdr.hu, then take the following steps:
# 1. Register at: http://sdr.hu/register
# 2. You will get an unique key by email. Copy it and paste here:
sdrhu_key = ""
# 3. Set this setting to True to enable listing:
sdrhu_public_listing = False

# ==== DSP/RX settings ====
dsp_plugin="csdr"
fft_fps=15
fft_size=4096*4
samp_rate = 2700000
#samp_rate = 250000

upconverter_freq = 65529300

center_freq = 10000000+upconverter_freq
rf_gain = 0
ppm = 0 

audio_compression="adpcm" #valid values: "adpcm", "none" 
fft_compression="adpcm" #valid values: "adpcm", "none" 

start_rtl_thread=True 

# ==== I/Q sources (uncomment the appropriate) ====

# >> RTL-SDR via rtl_sdr 

start_rtl_command="rtl_sdr -s {samp_rate} -f {center_freq} -p {ppm} -g {rf_gain} - | nc -vvl 127.0.0.1 8888"
format_conversion="csdr convert_u8_f"

# >> Sound card SDR (needs ALSA)
#I did not have the chance to properly test it.
#samp_rate = 96000
#start_rtl_command="arecord -f S16_LE -r {samp_rate} -c2 - | nc -vvl 127.0.0.1 8888".format(samp_rate=samp_rate)
#format_conversion="csdr convert_i16_f | csdr gain_ff 30"

# >> RTL_SDR via rtl_tcp
#start_rtl_command="rtl_tcp -s {samp_rate} -f {center_freq} -g {rf_gain} -P {ppm} -p 8888".format(rf_gain=rf_gain, center_freq=center_freq, samp_rate=samp_rate, ppm=ppm)
#format_conversion="csdr convert_u8_f"

# >> /dev/urandom test signal source
#samp_rate = 2400000
#start_rtl_command="cat /dev/urandom | (pv -qL `python -c 'print int({samp_rate} * 2.2)'` 2>&1) | nc -vvl 127.0.0.1  8888".format(rf_gain=rf_gain, center_freq=center_freq, samp_rate=samp_rate)
#format_conversion="csdr convert_u8_f"

#You can use other SDR hardware as well, by giving your own command that outputs the I/Q samples...

shown_center_freq = center_freq-upconverter_freq #you can change this if you use an upconverter

client_audio_buffer_size = 5
#increasing client_audio_buffer_size will:
# - also increase the latency 
# - decrease the chance of audio underruns

start_freq = center_freq
start_mod = "nfm" #nfm, am, lsb, usb, cw

iq_server_port = 4951
# (if ncat is not available on your system, rtl_mus will be used, thus you will have to set the same port as "my_listening_port" in config_rtl.py as well)
