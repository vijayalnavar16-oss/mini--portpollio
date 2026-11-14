/**
 * MULTI-FUNCTIONAL SMART AUTOMOTIVE SAFETY SYSTEM USING ESP32
 * College Mini-Project Interactive Logic & Portfolio Scripts
 */

document.addEventListener("DOMContentLoaded", () => {
  initNavigation();
  initBackToTop();
  initSimulator();
});

/* ===================================================================
   1. NAVIGATION & SCROLL HANDLING
   =================================================================== */
function initNavigation() {
  const navToggle = document.getElementById("navToggle");
  const navLinks = document.getElementById("navLinks");
  const links = document.querySelectorAll(".nav-link");

  if (navToggle && navLinks) {
    navToggle.addEventListener("click", () => {
      navLinks.classList.toggle("open");
    });
  }

  // Smooth scroll and close menu
  links.forEach(link => {
    link.addEventListener("click", (e) => {
      const targetId = link.getAttribute("href");
      if (targetId && targetId.startsWith("#")) {
        e.preventDefault();
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          const navOffset = 80;
          const elementPosition = targetElement.getBoundingClientRect().top;
          const offsetPosition = elementPosition + window.pageYOffset - navOffset;

          window.scrollTo({
            top: offsetPosition,
            behavior: "smooth"
          });

          if (navLinks) navLinks.classList.remove("open");
        }
      }
    });
  });

  // Scrollspy to highlight active nav link
  const sections = document.querySelectorAll("section[id]");
  window.addEventListener("scroll", () => {
    let current = "";
    const scrollY = window.pageYOffset;

    sections.forEach(section => {
      const sectionHeight = section.offsetHeight;
      const sectionTop = section.offsetTop - 120;
      const sectionId = section.getAttribute("id");

      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
        current = sectionId;
      }
    });

    links.forEach(link => {
      link.classList.remove("active");
      if (link.getAttribute("href") === `#${current}`) {
        link.classList.add("active");
      }
    });
  });
}

/* ===================================================================
   2. BACK TO TOP BUTTON
   =================================================================== */
function initBackToTop() {
  const backToTopBtn = document.getElementById("backToTop");
  if (!backToTopBtn) return;

  window.addEventListener("scroll", () => {
    if (window.pageYOffset > 400) {
      backToTopBtn.classList.add("visible");
    } else {
      backToTopBtn.classList.remove("visible");
    }
  });

  backToTopBtn.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  });
}

/* ===================================================================
   3. INTERACTIVE LOGIC SIMULATOR (EDUCATIONAL STATE MACHINE)
   Demonstrates firmware logic and threshold evaluation in browser.
   Explicitly for academic visualization - not real hardware.
   =================================================================== */
function initSimulator() {
  // Input elements
  const sliderFront = document.getElementById("sliderFront");
  const sliderLeft = document.getElementById("sliderLeft");
  const sliderRight = document.getElementById("sliderRight");
  const sliderLight = document.getElementById("sliderLight");
  
  const valFront = document.getElementById("valFront");
  const valLeft = document.getElementById("valLeft");
  const valRight = document.getElementById("valRight");
  const valLight = document.getElementById("valLight");

  const btnShock = document.getElementById("btnSimShock");
  const btnEstop = document.getElementById("btnSimEstop");
  const btnReset = document.getElementById("btnSimReset");

  // Telemetry output elements
  const telemMcuState = document.getElementById("telemMcuState");
  const telemMotors = document.getElementById("telemMotors");
  const telemHeadlights = document.getElementById("telemHeadlights");
  const telemBlindspotL = document.getElementById("telemBlindspotL");
  const telemBlindspotR = document.getElementById("telemBlindspotR");
  const telemBuzzer = document.getElementById("telemBuzzer");

  // SVG Diagram elements
  const svgHeadlightL = document.getElementById("svgHeadlightL");
  const svgHeadlightR = document.getElementById("svgHeadlightR");
  const svgBlindspotL = document.getElementById("svgBlindspotL");
  const svgBlindspotR = document.getElementById("svgBlindspotR");
  const svgBuzzer = document.getElementById("svgBuzzer");
  const svgMotorL = document.getElementById("svgMotorL");
  const svgMotorR = document.getElementById("svgMotorR");
  const svgSonarFront = document.getElementById("svgSonarFront");

  // State flags
  let isImpactTriggered = false;
  let isEstopTriggered = false;

  // Threshold Constants
  const DIST_FRONT_THRESHOLD = 15; // cm (App 1: Obstacle Stopping)
  const DIST_BLINDSPOT_THRESHOLD = 20; // cm (App 2: Blind Spot Detection)
  const LIGHT_LUX_THRESHOLD = 40; // % (App 3: Automatic Headlights)

  function updateSimulation() {
    const frontDist = parseInt(sliderFront.value, 10);
    const leftDist = parseInt(sliderLeft.value, 10);
    const rightDist = parseInt(sliderRight.value, 10);
    const lightLevel = parseInt(sliderLight.value, 10);

    // Update readout texts
    valFront.textContent = `${frontDist} cm`;
    valLeft.textContent = `${leftDist} cm`;
    valRight.textContent = `${rightDist} cm`;
    valLight.textContent = `${lightLevel}%`;

    // 1. App 3: Automatic Headlight Control Logic
    // Low light condition (< 40%) turns Headlights ON, sufficient light turns OFF
    const isHeadlightsOn = lightLevel < LIGHT_LUX_THRESHOLD;
    if (isHeadlightsOn) {
      telemHeadlights.textContent = "ON (Low Ambient Light)";
      telemHeadlights.style.color = "#38bdf8";
      if (svgHeadlightL) svgHeadlightL.classList.add("on");
      if (svgHeadlightR) svgHeadlightR.classList.add("on");
    } else {
      telemHeadlights.textContent = "OFF (Daylight Sufficient)";
      telemHeadlights.style.color = "#94a3b8";
      if (svgHeadlightL) svgHeadlightL.classList.remove("on");
      if (svgHeadlightR) svgHeadlightR.classList.remove("on");
    }

    // 2. App 2: Blind Spot Detection Logic
    // Left & Right ultrasonic sensors trigger corresponding LEDs when proximity <= 20cm
    const isLeftBlindspotWarning = leftDist <= DIST_BLINDSPOT_THRESHOLD;
    if (isLeftBlindspotWarning) {
      telemBlindspotL.textContent = "ALERT: Vehicle in Left Zone";
      telemBlindspotL.style.color = "#fbbf24";
      if (svgBlindspotL) svgBlindspotL.classList.add("active");
    } else {
      telemBlindspotL.textContent = "CLEAR";
      telemBlindspotL.style.color = "#94a3b8";
      if (svgBlindspotL) svgBlindspotL.classList.remove("active");
    }

    const isRightBlindspotWarning = rightDist <= DIST_BLINDSPOT_THRESHOLD;
    if (isRightBlindspotWarning) {
      telemBlindspotR.textContent = "ALERT: Vehicle in Right Zone";
      telemBlindspotR.style.color = "#fbbf24";
      if (svgBlindspotR) svgBlindspotR.classList.add("active");
    } else {
      telemBlindspotR.textContent = "CLEAR";
      telemBlindspotR.style.color = "#94a3b8";
      if (svgBlindspotR) svgBlindspotR.classList.remove("active");
    }

    // 3. App 1 & App 4 & E-Stop: Motor and Buzzer Arbitration
    const isObstacleTooClose = frontDist <= DIST_FRONT_THRESHOLD;

    // Update Sonar Visual Color
    if (svgSonarFront) {
      if (isObstacleTooClose) {
        svgSonarFront.setAttribute("stroke", "#ef4444");
      } else {
        svgSonarFront.setAttribute("stroke", "#10b981");
      }
    }

    // Master safety state evaluation
    if (isEstopTriggered) {
      // Emergency Stop overrides everything
      telemMcuState.textContent = "EMERGENCY STOP (MANUAL OVERRIDE)";
      telemMcuState.className = "sim-mcu-state-badge state-halted";
      
      telemMotors.textContent = "HALTED (L298N Inhibited: 0V)";
      telemMotors.style.color = "#ef4444";
      
      telemBuzzer.textContent = "ACTIVE SIREN (E-Stop Alarm)";
      telemBuzzer.style.color = "#ef4444";
      if (svgBuzzer) svgBuzzer.classList.add("alarm");

      setMotorsVisual(false);

    } else if (isImpactTriggered) {
      // App 4: Prototype Accident Detection Demonstration
      telemMcuState.textContent = "ABNORMAL IMPACT EVENT DETECTED (MPU6050)";
      telemMcuState.className = "sim-mcu-state-badge state-halted";
      
      telemMotors.textContent = "CUTOFF (Safety Lock Engaged)";
      telemMotors.style.color = "#ef4444";
      
      telemBuzzer.textContent = "CONTINUOUS ALARM (Impact State)";
      telemBuzzer.style.color = "#ef4444";
      if (svgBuzzer) svgBuzzer.classList.add("alarm");

      setMotorsVisual(false);

    } else if (isObstacleTooClose) {
      // App 1: Obstacle Detection and Automatic Stopping
      telemMcuState.textContent = "OBSTACLE HAZARD STOP (App 1 Active)";
      telemMcuState.className = "sim-mcu-state-badge state-hazard";
      
      telemMotors.textContent = "STOPPED (Distance < 15cm)";
      telemMotors.style.color = "#f59e0b";
      
      telemBuzzer.textContent = "WARNING BEEPING (Obstacle Alert)";
      telemBuzzer.style.color = "#f59e0b";
      if (svgBuzzer) svgBuzzer.classList.add("alarm");

      setMotorsVisual(false);

    } else {
      // Normal nominal running state
      telemMcuState.textContent = "NORMAL RUNNING / MONITORING";
      telemMcuState.className = "sim-mcu-state-badge state-normal";
      
      telemMotors.textContent = "RUNNING FORWARD (L298N Active)";
      telemMotors.style.color = "#10b981";
      
      telemBuzzer.textContent = "MUTED (Path Clear)";
      telemBuzzer.style.color = "#94a3b8";
      if (svgBuzzer) svgBuzzer.classList.remove("alarm");

      setMotorsVisual(true);
    }
  }

  function setMotorsVisual(isRunning) {
    if (svgMotorL && svgMotorR) {
      if (isRunning) {
        svgMotorL.setAttribute("fill", "#10b981");
        svgMotorR.setAttribute("fill", "#10b981");
      } else {
        svgMotorL.setAttribute("fill", "#ef4444");
        svgMotorR.setAttribute("fill", "#ef4444");
      }
    }
  }

  // Event Listeners for Sliders
  [sliderFront, sliderLeft, sliderRight, sliderLight].forEach(slider => {
    if (slider) {
      slider.addEventListener("input", updateSimulation);
    }
  });

  // Trigger Impact (App 4 Simulation)
  if (btnShock) {
    btnShock.addEventListener("click", () => {
      isImpactTriggered = true;
      updateSimulation();
    });
  }

  // Trigger E-Stop
  if (btnEstop) {
    btnEstop.addEventListener("click", () => {
      isEstopTriggered = true;
      updateSimulation();
    });
  }

  // Reset to default
  if (btnReset) {
    btnReset.addEventListener("click", () => {
      isImpactTriggered = false;
      isEstopTriggered = false;
      sliderFront.value = 45;
      sliderLeft.value = 50;
      sliderRight.value = 50;
      sliderLight.value = 75;
      updateSimulation();
    });
  }

  // Initial update
  updateSimulation();
}
