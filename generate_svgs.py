"""
Script to generate crisp, technical SVG illustrations for the 11 hardware components.
"""
import os

os.makedirs("assets", exist_ok=True)

# 1. ESP32-WROOM-32
esp32_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <defs>
    <linearGradient id="pcbGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#94a3b8"/>
      <stop offset="50%" stop-color="#cbd5e1"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
    <linearGradient id="goldPin" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <!-- Board PCB -->
  <rect x="30" y="20" width="260" height="180" rx="10" fill="url(#pcbGrad)" stroke="#38bdf8" stroke-width="2"/>
  <!-- Mounting holes -->
  <circle cx="45" cy="35" r="5" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
  <circle cx="275" cy="35" r="5" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
  <circle cx="45" cy="185" r="5" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
  <circle cx="275" cy="185" r="5" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
  <!-- Top Pin Header (15 pins) -->
  <g fill="url(#goldPin)">
    <!-- 15 pins across top -->
    <rect x="55" y="10" width="8" height="16" rx="1"/><rect x="70" y="10" width="8" height="16" rx="1"/>
    <rect x="85" y="10" width="8" height="16" rx="1"/><rect x="100" y="10" width="8" height="16" rx="1"/>
    <rect x="115" y="10" width="8" height="16" rx="1"/><rect x="130" y="10" width="8" height="16" rx="1"/>
    <rect x="145" y="10" width="8" height="16" rx="1"/><rect x="160" y="10" width="8" height="16" rx="1"/>
    <rect x="175" y="10" width="8" height="16" rx="1"/><rect x="190" y="10" width="8" height="16" rx="1"/>
    <rect x="205" y="10" width="8" height="16" rx="1"/><rect x="220" y="10" width="8" height="16" rx="1"/>
    <rect x="235" y="10" width="8" height="16" rx="1"/><rect x="250" y="10" width="8" height="16" rx="1"/>
    <rect x="265" y="10" width="8" height="16" rx="1"/>
  </g>
  <!-- Bottom Pin Header (15 pins) -->
  <g fill="url(#goldPin)">
    <rect x="55" y="194" width="8" height="16" rx="1"/><rect x="70" y="194" width="8" height="16" rx="1"/>
    <rect x="85" y="194" width="8" height="16" rx="1"/><rect x="100" y="194" width="8" height="16" rx="1"/>
    <rect x="115" y="194" width="8" height="16" rx="1"/><rect x="130" y="194" width="8" height="16" rx="1"/>
    <rect x="145" y="194" width="8" height="16" rx="1"/><rect x="160" y="194" width="8" height="16" rx="1"/>
    <rect x="175" y="194" width="8" height="16" rx="1"/><rect x="190" y="194" width="8" height="16" rx="1"/>
    <rect x="205" y="194" width="8" height="16" rx="1"/><rect x="220" y="194" width="8" height="16" rx="1"/>
    <rect x="235" y="194" width="8" height="16" rx="1"/><rect x="250" y="194" width="8" height="16" rx="1"/>
    <rect x="265" y="194" width="8" height="16" rx="1"/>
  </g>
  <!-- Micro USB Port on left -->
  <rect x="20" y="90" width="22" height="40" rx="3" fill="#64748b" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="22" y="98" width="10" height="24" rx="1" fill="#1e293b"/>
  <!-- CP2102 / CH340 Chip -->
  <rect x="55" y="95" width="24" height="30" rx="2" fill="#020617" stroke="#475569" stroke-width="1"/>
  <!-- Buttons (EN / BOOT) -->
  <rect x="42" y="55" width="16" height="14" rx="2" fill="#334155" stroke="#94a3b8" stroke-width="1"/>
  <circle cx="50" cy="62" r="3" fill="#cbd5e1"/>
  <text x="50" y="78" fill="#94a3b8" font-size="7" font-family="monospace" text-anchor="middle">EN</text>
  <rect x="42" y="150" width="16" height="14" rx="2" fill="#334155" stroke="#94a3b8" stroke-width="1"/>
  <circle cx="50" cy="157" r="3" fill="#cbd5e1"/>
  <text x="50" y="173" fill="#94a3b8" font-size="7" font-family="monospace" text-anchor="middle">BOOT</text>
  <!-- ESP-WROOM-32 Metal Shield Can -->
  <rect x="120" y="60" width="140" height="100" rx="5" fill="url(#shieldGrad)" stroke="#475569" stroke-width="2"/>
  <!-- PCB Antenna trace section at right -->
  <path d="M 235 70 L 250 70 L 250 80 L 240 80 L 240 90 L 250 90 L 250 100 L 240 100 L 240 110 L 250 110 L 250 120 L 240 120 L 240 130 L 250 130 L 250 145 L 235 145" fill="none" stroke="#d97706" stroke-width="2"/>
  <!-- Shield Text -->
  <text x="175" y="92" fill="#0f172a" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">ESP-WROOM-32</text>
  <text x="175" y="108" fill="#334155" font-size="9" font-family="monospace" text-anchor="middle">Espressif Systems</text>
  <text x="175" y="124" fill="#1e293b" font-size="8" font-family="monospace" text-anchor="middle">Wi-Fi &amp; BT MCU (30 Pin)</text>
  <circle cx="135" cy="75" r="4" fill="#0284c7"/>
  <!-- Onboard LEDs -->
  <rect x="88" y="102" width="6" height="6" fill="#ef4444" rx="1"/>
  <text x="91" y="97" fill="#ef4444" font-size="6" font-family="monospace" text-anchor="middle">PWR</text>
  <rect x="88" y="118" width="6" height="6" fill="#06b6d4" rx="1"/>
  <text x="91" y="132" fill="#06b6d4" font-size="6" font-family="monospace" text-anchor="middle">IO2</text>
</svg>'''

# 2. HC-SR04 Ultrasonic Sensor
ultrasonic_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <defs>
    <linearGradient id="sonarPcb" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="transducerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="50%" stop-color="#cbd5e1"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
  </defs>
  <!-- Blue PCB -->
  <rect x="35" y="45" width="250" height="130" rx="8" fill="url(#sonarPcb)" stroke="#38bdf8" stroke-width="2"/>
  <!-- Mounting corner holes -->
  <circle cx="48" cy="58" r="4" fill="#0c4a6e" stroke="#7dd3fc" stroke-width="1.5"/>
  <circle cx="272" cy="58" r="4" fill="#0c4a6e" stroke="#7dd3fc" stroke-width="1.5"/>
  <circle cx="48" cy="162" r="4" fill="#0c4a6e" stroke="#7dd3fc" stroke-width="1.5"/>
  <circle cx="272" cy="162" r="4" fill="#0c4a6e" stroke="#7dd3fc" stroke-width="1.5"/>
  <!-- Left Transducer (Transmitter 'T') -->
  <circle cx="100" cy="110" r="45" fill="url(#transducerGrad)" stroke="#334155" stroke-width="3"/>
  <circle cx="100" cy="110" r="36" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
  <!-- Mesh Pattern -->
  <circle cx="100" cy="110" r="28" fill="none" stroke="#64748b" stroke-dasharray="2,2"/>
  <text x="100" y="116" fill="#f8fafc" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">T</text>
  <!-- Right Transducer (Receiver 'R') -->
  <circle cx="220" cy="110" r="45" fill="url(#transducerGrad)" stroke="#334155" stroke-width="3"/>
  <circle cx="220" cy="110" r="36" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
  <circle cx="220" cy="110" r="28" fill="none" stroke="#64748b" stroke-dasharray="2,2"/>
  <text x="220" y="116" fill="#f8fafc" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">R</text>
  <!-- Crystal Oscillator -->
  <rect x="150" y="70" width="20" height="12" rx="3" fill="#cbd5e1" stroke="#475569" stroke-width="1"/>
  <text x="160" y="79" fill="#1e293b" font-size="6" font-family="monospace" text-anchor="middle">4MHz</text>
  <!-- Label -->
  <text x="160" y="105" fill="#f8fafc" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">HC-SR04</text>
  <!-- Pin Header at Bottom Center -->
  <rect x="125" y="165" width="70" height="20" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
  <!-- 4 Header Pins -->
  <rect x="135" y="180" width="6" height="16" rx="1" fill="#f59e0b"/>
  <rect x="150" y="180" width="6" height="16" rx="1" fill="#f59e0b"/>
  <rect x="165" y="180" width="6" height="16" rx="1" fill="#f59e0b"/>
  <rect x="180" y="180" width="6" height="16" rx="1" fill="#f59e0b"/>
  <!-- Pin Labels -->
  <text x="138" y="160" fill="#bae6fd" font-size="7" font-family="monospace" text-anchor="middle">VCC</text>
  <text x="153" y="160" fill="#bae6fd" font-size="7" font-family="monospace" text-anchor="middle">TRIG</text>
  <text x="168" y="160" fill="#bae6fd" font-size="7" font-family="monospace" text-anchor="middle">ECHO</text>
  <text x="183" y="160" fill="#bae6fd" font-size="7" font-family="monospace" text-anchor="middle">GND</text>
</svg>'''

# 3. MPU6050 6-Axis IMU
mpu6050_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <defs>
    <linearGradient id="mpuPcb" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#1e3a8a"/>
    </linearGradient>
  </defs>
  <!-- Blue Breakout Board -->
  <rect x="50" y="30" width="220" height="160" rx="8" fill="url(#mpuPcb)" stroke="#38bdf8" stroke-width="2"/>
  <!-- Mounting corner holes -->
  <circle cx="65" cy="45" r="5" fill="#0f172a" stroke="#7dd3fc" stroke-width="1.5"/>
  <circle cx="255" cy="45" r="5" fill="#0f172a" stroke="#7dd3fc" stroke-width="1.5"/>
  <!-- Central MPU6050 IC (QFN) -->
  <rect x="125" y="80" width="70" height="70" rx="4" fill="#0f172a" stroke="#475569" stroke-width="2"/>
  <!-- Chip Pin Indicators -->
  <circle cx="137" cy="92" r="3" fill="#cbd5e1"/>
  <text x="160" y="115" fill="#f8fafc" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">MPU-6050</text>
  <text x="160" y="130" fill="#94a3b8" font-size="7" font-family="monospace" text-anchor="middle">6-DOF IMU</text>
  <!-- Orientation Axes Indicator -->
  <g stroke="#22d3ee" stroke-width="1.5" fill="none">
    <line x1="80" y1="120" x2="105" y2="120" marker-end="url(#arrow)"/>
    <line x1="80" y1="120" x2="80" y2="95"/>
    <circle cx="80" cy="120" r="2" fill="#22d3ee"/>
  </g>
  <text x="110" y="123" fill="#22d3ee" font-size="8" font-family="monospace">X</text>
  <text x="80" y="88" fill="#22d3ee" font-size="8" font-family="monospace">Y</text>
  <text x="70" y="135" fill="#22d3ee" font-size="8" font-family="monospace">⊙ Z</text>
  <!-- Power LED -->
  <rect x="220" y="65" width="8" height="6" fill="#ef4444" rx="1"/>
  <text x="224" y="60" fill="#f87171" font-size="7" font-family="monospace" text-anchor="middle">PWR</text>
  <!-- 3.3V LDO Voltage Regulator -->
  <rect x="215" y="95" width="20" height="15" rx="1" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
  <!-- Board Name -->
  <text x="160" y="55" fill="#f0f9ff" font-size="12" font-family="monospace" font-weight="bold" text-anchor="middle">GY-521 BREAKOUT</text>
  <!-- Pin Header at Bottom (8 pins) -->
  <g fill="#f59e0b">
    <rect x="70" y="180" width="8" height="16" rx="1"/><rect x="90" y="180" width="8" height="16" rx="1"/>
    <rect x="110" y="180" width="8" height="16" rx="1"/><rect x="130" y="180" width="8" height="16" rx="1"/>
    <rect x="150" y="180" width="8" height="16" rx="1"/><rect x="170" y="180" width="8" height="16" rx="1"/>
    <rect x="190" y="180" width="8" height="16" rx="1"/><rect x="210" y="180" width="8" height="16" rx="1"/>
  </g>
  <g fill="#bae6fd" font-size="6" font-family="monospace" text-anchor="middle">
    <text x="74" y="174">VCC</text><text x="94" y="174">GND</text>
    <text x="114" y="174">SCL</text><text x="134" y="174">SDA</text>
    <text x="154" y="174">XDA</text><text x="174" y="174">XCL</text>
    <text x="194" y="174">AD0</text><text x="214" y="174">INT</text>
  </g>
</svg>'''

# 4. LDR Light Sensor Module
ldr_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <defs>
    <linearGradient id="ldrPcb" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0369a1"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <!-- Blue PCB -->
  <rect x="40" y="45" width="240" height="130" rx="8" fill="url(#ldrPcb)" stroke="#38bdf8" stroke-width="2"/>
  <!-- LDR Photoresistor Element (Protruding Left) -->
  <line x1="40" y1="95" x2="18" y2="95" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="125" x2="18" y2="125" stroke="#94a3b8" stroke-width="2"/>
  <rect x="8" y="85" width="15" height="50" rx="4" fill="#fde047" stroke="#b45309" stroke-width="2"/>
  <path d="M 12 92 C 16 95, 16 97, 12 100 C 16 103, 16 105, 12 108 C 16 111, 16 113, 12 116 C 16 119, 16 121, 12 124" fill="none" stroke="#dc2626" stroke-width="2"/>
  <text x="15" y="75" fill="#fef08a" font-size="8" font-family="monospace" text-anchor="middle">LDR</text>
  <!-- LM393 Comparator IC -->
  <rect x="120" y="90" width="45" height="40" rx="2" fill="#020617" stroke="#475569" stroke-width="1.5"/>
  <text x="142" y="112" fill="#f8fafc" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">LM393</text>
  <text x="142" y="122" fill="#94a3b8" font-size="6" font-family="monospace" text-anchor="middle">Comparator</text>
  <!-- Sensitivity Potentiometer (Blue square with brass screw) -->
  <rect x="65" y="85" width="40" height="45" rx="3" fill="#2563eb" stroke="#1d4ed8" stroke-width="2"/>
  <circle cx="85" cy="107" r="12" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
  <line x1="77" y1="107" x2="93" y2="107" stroke="#451a03" stroke-width="2.5"/>
  <text x="85" y="77" fill="#93c5fd" font-size="7" font-family="monospace" text-anchor="middle">TRIMMER</text>
  <!-- Indicator LEDs -->
  <rect x="180" y="85" width="8" height="6" fill="#ef4444" rx="1"/>
  <text x="184" y="78" fill="#f87171" font-size="6" font-family="monospace" text-anchor="middle">PWR</text>
  <rect x="180" y="125" width="8" height="6" fill="#22c55e" rx="1"/>
  <text x="184" y="140" fill="#4ade80" font-size="6" font-family="monospace" text-anchor="middle">DO_LED</text>
  <!-- Header Pins on Right -->
  <g fill="#f59e0b">
    <rect x="268" y="70" width="16" height="6" rx="1"/>
    <rect x="268" y="90" width="16" height="6" rx="1"/>
    <rect x="268" y="110" width="16" height="6" rx="1"/>
    <rect x="268" y="130" width="16" height="6" rx="1"/>
  </g>
  <g fill="#bae6fd" font-size="7" font-family="monospace" text-anchor="end">
    <text x="260" y="76">VCC</text>
    <text x="260" y="96">GND</text>
    <text x="260" y="116">DO</text>
    <text x="260" y="136">AO</text>
  </g>
  <!-- Module Title -->
  <text x="160" y="65" fill="#f0f9ff" font-size="11" font-family="monospace" font-weight="bold" text-anchor="middle">LIGHT SENSOR MODULE</text>
</svg>'''

# 5. L298N Dual H-Bridge Motor Driver
l298n_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <defs>
    <linearGradient id="driverPcb" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#991b1b"/>
      <stop offset="100%" stop-color="#450a0a"/>
    </linearGradient>
    <linearGradient id="heatsinkGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="50%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <!-- Red PCB -->
  <rect x="35" y="25" width="250" height="170" rx="8" fill="url(#driverPcb)" stroke="#f87171" stroke-width="2"/>
  <!-- Mounting corner holes -->
  <circle cx="48" cy="38" r="4" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5"/>
  <circle cx="272" cy="38" r="4" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5"/>
  <circle cx="48" cy="182" r="4" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5"/>
  <circle cx="272" cy="182" r="4" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5"/>
  <!-- Large Black Finned Heat Sink -->
  <rect x="100" y="40" width="120" height="75" rx="3" fill="url(#heatsinkGrad)" stroke="#64748b" stroke-width="1.5"/>
  <!-- Heatsink Fins -->
  <line x1="115" y1="40" x2="115" y2="115" stroke="#475569" stroke-width="3"/>
  <line x1="130" y1="40" x2="130" y2="115" stroke="#475569" stroke-width="3"/>
  <line x1="145" y1="40" x2="145" y2="115" stroke="#475569" stroke-width="3"/>
  <line x1="160" y1="40" x2="160" y2="115" stroke="#475569" stroke-width="3"/>
  <line x1="175" y1="40" x2="175" y2="115" stroke="#475569" stroke-width="3"/>
  <line x1="190" y1="40" x2="190" y2="115" stroke="#475569" stroke-width="3"/>
  <line x1="205" y1="40" x2="205" y2="115" stroke="#475569" stroke-width="3"/>
  <rect x="125" y="115" width="70" height="15" rx="2" fill="#020617"/>
  <text x="160" y="126" fill="#f8fafc" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">L298N DUAL H-BRIDGE</text>
  <!-- Screw Terminal Block Left (Motor A) -->
  <rect x="42" y="75" width="28" height="45" rx="2" fill="#15803d" stroke="#166534" stroke-width="1.5"/>
  <circle cx="56" cy="88" r="4" fill="#020617" stroke="#e2e8f0" stroke-width="1"/>
  <circle cx="56" cy="107" r="4" fill="#020617" stroke="#e2e8f0" stroke-width="1"/>
  <text x="56" y="68" fill="#bbf7d0" font-size="7" font-family="monospace" text-anchor="middle">OUT1/2</text>
  <!-- Screw Terminal Block Right (Motor B) -->
  <rect x="250" y="75" width="28" height="45" rx="2" fill="#15803d" stroke="#166534" stroke-width="1.5"/>
  <circle cx="264" cy="88" r="4" fill="#020617" stroke="#e2e8f0" stroke-width="1"/>
  <circle cx="264" cy="107" r="4" fill="#020617" stroke="#e2e8f0" stroke-width="1"/>
  <text x="264" y="68" fill="#bbf7d0" font-size="7" font-family="monospace" text-anchor="middle">OUT3/4</text>
  <!-- Power Terminal Block (12V, GND, 5V) -->
  <rect x="70" y="145" width="55" height="35" rx="2" fill="#15803d" stroke="#166534" stroke-width="1.5"/>
  <circle cx="80" cy="162" r="4" fill="#020617" stroke="#e2e8f0" stroke-width="1"/>
  <circle cx="97" cy="162" r="4" fill="#020617" stroke="#e2e8f0" stroke-width="1"/>
  <circle cx="114" cy="162" r="4" fill="#020617" stroke="#e2e8f0" stroke-width="1"/>
  <text x="80" y="190" fill="#fecaca" font-size="6" font-family="monospace" text-anchor="middle">12V</text>
  <text x="97" y="190" fill="#fecaca" font-size="6" font-family="monospace" text-anchor="middle">GND</text>
  <text x="114" y="190" fill="#fecaca" font-size="6" font-family="monospace" text-anchor="middle">+5V</text>
  <!-- Logic Control Header Pins (ENA, IN1, IN2, IN3, IN4, ENB) -->
  <rect x="155" y="150" width="90" height="20" fill="#020617" stroke="#475569" stroke-width="1"/>
  <g fill="#f59e0b">
    <rect x="162" y="155" width="6" height="10" rx="1"/><rect x="176" y="155" width="6" height="10" rx="1"/>
    <rect x="190" y="155" width="6" height="10" rx="1"/><rect x="204" y="155" width="6" height="10" rx="1"/>
    <rect x="218" y="155" width="6" height="10" rx="1"/><rect x="232" y="155" width="6" height="10" rx="1"/>
  </g>
  <text x="200" y="185" fill="#fecaca" font-size="7" font-family="monospace" text-anchor="middle">ENA IN1 IN2 IN3 IN4 ENB</text>
  <!-- 5V Onboard Regulator Jumper -->
  <rect x="135" y="148" width="10" height="15" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
</svg>'''

# 6. DC Geared Motors
dc_motor_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <defs>
    <linearGradient id="gearboxYellow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#facc15"/>
      <stop offset="100%" stop-color="#ca8a04"/>
    </linearGradient>
    <linearGradient id="motorMetal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e2e8f0"/>
      <stop offset="50%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
  </defs>
  <!-- Yellow Plastic Gearbox Housing -->
  <rect x="100" y="60" width="140" height="80" rx="8" fill="url(#gearboxYellow)" stroke="#a16207" stroke-width="2"/>
  <!-- Output Drive Shaft (White nylon flatted shaft) -->
  <rect x="240" y="90" width="30" height="20" rx="2" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/>
  <rect x="255" y="94" width="15" height="12" fill="#cbd5e1"/>
  <text x="270" y="82" fill="#38bdf8" font-size="8" font-family="monospace" text-anchor="middle">SHAFT</text>
  <!-- Internal Gear Details / Housing Fasteners -->
  <circle cx="130" cy="80" r="4" fill="#713f12"/>
  <circle cx="210" cy="80" r="4" fill="#713f12"/>
  <circle cx="130" cy="120" r="4" fill="#713f12"/>
  <circle cx="210" cy="120" r="4" fill="#713f12"/>
  <circle cx="170" cy="100" r="16" fill="none" stroke="#eab308" stroke-width="2" stroke-dasharray="3,3"/>
  <!-- Cylindrical DC Motor Canister (Silver) -->
  <rect x="40" y="70" width="60" height="60" rx="6" fill="url(#motorMetal)" stroke="#334155" stroke-width="2"/>
  <!-- Motor Terminals & Power Leads -->
  <rect x="30" y="82" width="10" height="6" fill="#f59e0b"/>
  <rect x="30" y="112" width="10" height="6" fill="#f59e0b"/>
  <!-- Red & Black Wires -->
  <path d="M 30 85 C 15 85, 10 50, 45 40" fill="none" stroke="#ef4444" stroke-width="3"/>
  <path d="M 30 115 C 15 115, 10 170, 50 175" fill="none" stroke="#020617" stroke-width="3"/>
  <!-- Labels -->
  <text x="70" y="105" fill="#0f172a" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">3-6V DC</text>
  <text x="170" y="104" fill="#451a03" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">TT GEARBOX</text>
  <text x="170" y="148" fill="#e2e8f0" font-size="9" font-family="monospace" text-anchor="middle">Gear Ratio 1:48 (Qty: 2 Motors)</text>
</svg>'''

# 7. Piezo Buzzer
buzzer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <defs>
    <radialGradient id="buzzerBody" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="70%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#020617"/>
    </radialGradient>
  </defs>
  <!-- Circular Buzzer Enclosure -->
  <circle cx="160" cy="110" r="70" fill="url(#buzzerBody)" stroke="#64748b" stroke-width="3"/>
  <!-- Inner Ring Step -->
  <circle cx="160" cy="110" r="50" fill="#0f172a" stroke="#475569" stroke-width="2"/>
  <!-- Sound Hole in Center -->
  <circle cx="160" cy="110" r="16" fill="#020617" stroke="#000000" stroke-width="3"/>
  <!-- Positive Terminal Mark '+' -->
  <text x="120" y="80" fill="#ef4444" font-size="24" font-family="sans-serif" font-weight="bold" text-anchor="middle">+</text>
  <!-- Audio Wave Rings (Simulated Alert) -->
  <path d="M 240 85 A 35 35 0 0 1 240 135" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 255 70 A 55 55 0 0 1 255 150" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-dasharray="4,3"/>
  <path d="M 270 55 A 75 75 0 0 1 270 165" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="3,3"/>
  <!-- Label -->
  <text x="160" y="150" fill="#94a3b8" font-size="9" font-family="monospace" text-anchor="middle">5V ACTIVE PIEZO</text>
  <text x="160" y="195" fill="#e2e8f0" font-size="9" font-family="monospace" text-anchor="middle">Acoustic Audio Alarm</text>
</svg>'''

# 8. LEDs (Headlights & Blind Spot Indicators)
led_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <defs>
    <!-- Cyan Headlight Glow -->
    <radialGradient id="cyanGlow" cx="50%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="40%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </radialGradient>
    <!-- Amber Blind Spot Glow -->
    <radialGradient id="amberGlow" cx="50%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="40%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </radialGradient>
  </defs>
  <!-- Headlight LED (Left) -->
  <g transform="translate(40, 20)">
    <!-- Rays -->
    <line x1="45" y1="30" x2="10" y2="10" stroke="#38bdf8" stroke-width="2"/>
    <line x1="45" y1="30" x2="45" y2="5" stroke="#38bdf8" stroke-width="2"/>
    <line x1="45" y1="30" x2="80" y2="10" stroke="#38bdf8" stroke-width="2"/>
    <!-- Dome -->
    <path d="M 25 70 L 25 50 A 20 20 0 0 1 65 50 L 65 70 Z" fill="url(#cyanGlow)" stroke="#7dd3fc" stroke-width="2"/>
    <rect x="22" y="70" width="46" height="6" rx="2" fill="#0284c7"/>
    <!-- Anode & Cathode Leads -->
    <line x1="35" y1="76" x2="35" y2="130" stroke="#94a3b8" stroke-width="2"/>
    <line x1="55" y1="76" x2="55" y2="115" stroke="#94a3b8" stroke-width="2"/>
    <text x="45" y="150" fill="#38bdf8" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">HEADLIGHT</text>
    <text x="45" y="162" fill="#94a3b8" font-size="7" font-family="monospace" text-anchor="middle">High-Lumen LED</text>
  </g>
  <!-- Blind Spot Indicator LED (Right) -->
  <g transform="translate(190, 20)">
    <!-- Rays -->
    <line x1="45" y1="30" x2="10" y2="10" stroke="#f59e0b" stroke-width="2"/>
    <line x1="45" y1="30" x2="45" y2="5" stroke="#f59e0b" stroke-width="2"/>
    <line x1="45" y1="30" x2="80" y2="10" stroke="#f59e0b" stroke-width="2"/>
    <!-- Dome -->
    <path d="M 25 70 L 25 50 A 20 20 0 0 1 65 50 L 65 70 Z" fill="url(#amberGlow)" stroke="#fde047" stroke-width="2"/>
    <rect x="22" y="70" width="46" height="6" rx="2" fill="#b45309"/>
    <!-- Anode & Cathode Leads -->
    <line x1="35" y1="76" x2="35" y2="130" stroke="#94a3b8" stroke-width="2"/>
    <line x1="55" y1="76" x2="55" y2="115" stroke="#94a3b8" stroke-width="2"/>
    <text x="45" y="150" fill="#fbbf24" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">BLIND SPOT</text>
    <text x="45" y="162" fill="#94a3b8" font-size="7" font-family="monospace" text-anchor="middle">Amber Warning LEDs</text>
  </g>
</svg>'''

# 9. Emergency Push Button
estop_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <defs>
    <linearGradient id="redMushroom" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="60%" stop-color="#b91c1c"/>
      <stop offset="100%" stop-color="#7f1d1d"/>
    </linearGradient>
    <linearGradient id="yellowCollar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#facc15"/>
      <stop offset="50%" stop-color="#fef08a"/>
      <stop offset="100%" stop-color="#ca8a04"/>
    </linearGradient>
  </defs>
  <!-- Lower Enclosure Base -->
  <rect x="90" y="125" width="140" height="65" rx="6" fill="#1e293b" stroke="#475569" stroke-width="2"/>
  <!-- Screw Mounts -->
  <circle cx="105" cy="140" r="4" fill="#0f172a" stroke="#94a3b8" stroke-width="1"/>
  <circle cx="215" cy="140" r="4" fill="#0f172a" stroke="#94a3b8" stroke-width="1"/>
  <!-- Yellow Safety Collar -->
  <ellipse cx="160" cy="120" rx="55" ry="18" fill="url(#yellowCollar)" stroke="#a16207" stroke-width="2"/>
  <text x="160" y="124" fill="#713f12" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">EMERGENCY STOP</text>
  <!-- Red Actuator Plunger / Mushroom Cap -->
  <path d="M 115 95 C 115 60, 205 60, 205 95 Z" fill="url(#redMushroom)" stroke="#991b1b" stroke-width="2"/>
  <ellipse cx="160" cy="95" rx="45" ry="16" fill="#dc2626" stroke="#991b1b" stroke-width="1.5"/>
  <!-- Mechanical Push Arrow -->
  <path d="M 160 50 L 160 70 M 153 63 L 160 70 L 167 63" fill="none" stroke="#fecaca" stroke-width="3" stroke-linecap="round"/>
  <!-- Status Text -->
  <text x="160" y="165" fill="#f87171" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">HARDWARE OVERRIDE</text>
  <text x="160" y="178" fill="#94a3b8" font-size="7" font-family="monospace" text-anchor="middle">Instant Motor Halt &amp; Warning</text>
</svg>'''

# 10. Battery / Motor Power Supply
battery_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <defs>
    <linearGradient id="batteryBody" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="50%" stop-color="#0369a1"/>
      <stop offset="100%" stop-color="#075985"/>
    </linearGradient>
  </defs>
  <!-- Dual 18650 Battery Pack Holder -->
  <rect x="70" y="55" width="180" height="110" rx="10" fill="#0f172a" stroke="#334155" stroke-width="2"/>
  <!-- Cell 1 -->
  <rect x="85" y="68" width="70" height="84" rx="6" fill="url(#batteryBody)" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="79" y="98" width="6" height="24" rx="2" fill="#cbd5e1"/>
  <text x="120" y="114" fill="#f0f9ff" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">CELL 1</text>
  <text x="120" y="126" fill="#7dd3fc" font-size="7" font-family="monospace" text-anchor="middle">3.7V Li-ion</text>
  <!-- Cell 2 -->
  <rect x="165" y="68" width="70" height="84" rx="6" fill="url(#batteryBody)" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="235" y="98" width="6" height="24" rx="2" fill="#cbd5e1"/>
  <text x="200" y="114" fill="#f0f9ff" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">CELL 2</text>
  <text x="200" y="126" fill="#7dd3fc" font-size="7" font-family="monospace" text-anchor="middle">3.7V Li-ion</text>
  <!-- Output Power Leads (Red +12V / +7.4V, Black GND) -->
  <path d="M 238 80 C 265 80, 280 60, 295 60" fill="none" stroke="#ef4444" stroke-width="3"/>
  <path d="M 238 140 C 265 140, 280 160, 295 160" fill="none" stroke="#020617" stroke-width="3"/>
  <text x="305" y="64" fill="#ef4444" font-size="9" font-family="monospace" font-weight="bold">VCC</text>
  <text x="305" y="164" fill="#94a3b8" font-size="9" font-family="monospace" font-weight="bold">GND</text>
  <!-- Title / Specs -->
  <text x="160" y="185" fill="#e2e8f0" font-size="9" font-family="monospace" text-anchor="middle">Dual Rail Power Supply (ESP32 + Motors)</text>
</svg>'''

# 11. Connecting Wires & Prototype Chassis
chassis_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="100%">
  <defs>
    <linearGradient id="chassisPlate" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="50%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <!-- 2WD Robot Chassis Plate (Top View Outline) -->
  <rect x="70" y="40" width="160" height="140" rx="15" fill="url(#chassisPlate)" stroke="#38bdf8" stroke-width="2"/>
  <!-- Front Caster Wheel Mount -->
  <rect x="75" y="95" width="25" height="30" rx="4" fill="#020617" stroke="#64748b" stroke-width="1.5"/>
  <circle cx="87" cy="110" r="8" fill="#94a3b8"/>
  <text x="87" y="136" fill="#cbd5e1" font-size="6" font-family="monospace" text-anchor="middle">CASTER</text>
  <!-- Left Drive Wheel -->
  <rect x="180" y="20" width="45" height="24" rx="4" fill="#020617" stroke="#475569" stroke-width="2"/>
  <line x1="190" y1="20" x2="190" y2="44" stroke="#64748b" stroke-width="2"/>
  <line x1="200" y1="20" x2="200" y2="44" stroke="#64748b" stroke-width="2"/>
  <line x1="210" y1="20" x2="210" y2="44" stroke="#64748b" stroke-width="2"/>
  <!-- Right Drive Wheel -->
  <rect x="180" y="176" width="45" height="24" rx="4" fill="#020617" stroke="#475569" stroke-width="2"/>
  <line x1="190" y1="176" x2="190" y2="200" stroke="#64748b" stroke-width="2"/>
  <line x1="200" y1="176" x2="200" y2="200" stroke="#64748b" stroke-width="2"/>
  <line x1="210" y1="176" x2="210" y2="200" stroke="#64748b" stroke-width="2"/>
  <!-- Standoffs / Mounting Slots -->
  <rect x="130" y="60" width="60" height="40" rx="4" fill="none" stroke="#64748b" stroke-dasharray="3,3"/>
  <text x="160" y="82" fill="#94a3b8" font-size="7" font-family="monospace" text-anchor="middle">ESP32 MOUNT</text>
  <!-- Jumper Wires Bundles (Color Coded Ribbons) -->
  <path d="M 120 130 C 140 145, 170 120, 200 135" fill="none" stroke="#3b82f6" stroke-width="2"/>
  <path d="M 120 133 C 140 148, 170 123, 200 138" fill="none" stroke="#ef4444" stroke-width="2"/>
  <path d="M 120 136 C 140 151, 170 126, 200 141" fill="none" stroke="#10b981" stroke-width="2"/>
  <path d="M 120 139 C 140 154, 170 129, 200 144" fill="none" stroke="#eab308" stroke-width="2"/>
  <text x="160" y="160" fill="#bae6fd" font-size="7" font-family="monospace" text-anchor="middle">Dupont Jumper Harness</text>
  <text x="160" y="202" fill="#e2e8f0" font-size="9" font-family="monospace" text-anchor="middle">2WD Prototype Chassis Plate</text>
</svg>'''

svgs = {
    "assets/esp32.svg": esp32_svg,
    "assets/ultrasonic.svg": ultrasonic_svg,
    "assets/mpu6050.svg": mpu6050_svg,
    "assets/ldr.svg": ldr_svg,
    "assets/l298n.svg": l298n_svg,
    "assets/dc-motor.svg": dc_motor_svg,
    "assets/buzzer.svg": buzzer_svg,
    "assets/led.svg": led_svg,
    "assets/estop.svg": estop_svg,
    "assets/battery.svg": battery_svg,
    "assets/chassis.svg": chassis_svg,
}

for path, content in svgs.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated {path}")
