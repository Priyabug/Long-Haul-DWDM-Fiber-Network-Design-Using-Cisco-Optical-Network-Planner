# Long-Haul-DWDM-Fiber-Network-Design-Using-Cisco-Optical-Network-Planner

Designed a scalable, high-capacity Dense Wavelength Division Multiplexing (DWDM) transport system for a simulated 1,000 km fiber route using Cisco's Optical Network Planner. The project focused on optimizing spectral efficiency, minimizing signal degradation, and ensuring resiliency and reach across the optical backbone.


## 🎯 Project Objectives: Long-Haul DWDM Backbone Design

- 🚀 **Design a scalable DWDM backbone** capable of supporting both **100 Gbps** and **400 Gbps** wavelength services across long-haul fiber routes.

- 📊 **Evaluate optical performance metrics**, including:
  - Optical Power Budget
  - OSNR (Optical Signal-to-Noise Ratio)
  - Chromatic Dispersion

- 🔧 **Simulate amplifier placement** and **span loss compensation** for each fiber segment to ensure signal integrity across the entire route.

- 📦 **Translate the design** into **vendor-aligned configurations** suitable for real-world deployment (e.g., TL1 commands, ROADM planning, and interface parameters).


## 🛠️ Tools & Technologies

- 🧠 **Cisco Optical Network Planner (ONP)**  
  Used for professional-grade DWDM topology design and simulation.

- 🐍 **GNPy (Gaussian Noise Python)**  
  Open-source optical planner used to cross-verify span loss, OSNR, and reach.

- 📦 **DWDM Line Cards & ROADMs** *(Simulated)*  
  Emulated hardware configurations for realistic network modeling.

- 📊 **Excel + Python**  
  Utilized for optical power budgeting, loss calculations, and data validation.

- 🌐 **ITU Grid Wavelength Planning**  
  Applied ITU-T G.694.1 standards to allocate and manage channel spacing.

- 📄 **TL1 Command Templates**  
  Created for provisioning and simulating circuit turn-up in a vendor-aligned format.


  ## 🐍 🧪 GNPy (Gaussian Noise Python)

Successfully installed and launched **GNPy** using Docker:

```bash
$ docker run -it --rm --volume $(pwd):/shared telecominfraproject/oopt-gnpy
root@bea050f186f7:/shared/example-data#
````

## 🧪 What You Can Simulate with GNPy

GNPy empowers you to model and validate complex optical transport networks with features like:

- 🔀 **Optical Channel Planning**  
  Design wavelength routes across a DWDM network using standard ITU grid spacing.

- 📉 **Span Loss Calculation**  
  Accurately compute fiber attenuation over long-haul spans with customizable parameters.

- 📊 **OSNR Degradation Analysis**  
  Simulate the signal-to-noise ratio across spans to validate quality thresholds for 100G/400G.

- ⚡ **Amplifier Placement Optimization**  
  Determine the optimal positioning and gain settings of EDFAs or Raman amplifiers.
