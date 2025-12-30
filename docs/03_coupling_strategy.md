# Coupling Strategy

This document describes the numerical coupling strategy used to integrate
wind, wave, structural dynamics, and solar energy models into a single
simulation framework.

The goal is to ensure **physical consistency**, **numerical stability**,
and **modular extensibility**.

---

## 1. Coupling Philosophy

The platform uses a **partitioned coupling approach** rather than a fully
monolithic solver.

Each physical subsystem is solved independently:
- Wind field
- Wave and current field
- Platform structural dynamics
- Energy production modules

Coupling is enforced through a time-marching exchange of forces, motions,
and environmental states.

This approach:
- Reduces computational cost
- Simplifies development
- Allows independent validation

---

## 2. Global Time Loop

All modules are synchronized using a global time loop:

For each time step n → n+1:

1. Update environmental conditions
2. Solve wind field
3. Compute turbine aerodynamic forces
4. Solve wave and current loads
5. Update platform motion
6. Update solar orientation and power
7. Store outputs

Time discretization:
- Explicit coupling
- Fixed or adaptive time step

---

## 3. Data Exchange Between Modules

### 3.1 Wind → Structure

Transferred quantities:
- Thrust force
- Torque
- Turbulence intensity
- Wake velocity deficit

These forces act on:
- Turbine nacelle
- Tower
- Platform center of mass

---

### 3.2 Wave → Structure

Transferred quantities:
- Hydrodynamic forces
- Added mass
- Radiation damping
- Hydrostatic restoring forces

Wave kinematics are evaluated at structural nodes.

---

### 3.3 Structure → Wind

Platform motion feedback:
- Surge, sway, heave
- Roll, pitch, yaw

Motion-induced velocity corrections are applied to the wind solver to
account for floating turbine effects.

---

### 3.4 Structure → Solar

Platform motion updates:
- Panel tilt angle
- Effective irradiance
- Shadowing from turbine tower

Solar power output is updated every time step.

---

## 4. Fixed vs Floating Platform Handling

### Fixed Platform:
- Structural motion constrained
- Wind and wave forces evaluated on static geometry

### Floating Platform:
- Full 6-DOF motion enabled
- Mooring forces included
- Motion feedback enabled for wind and solar modules

A single solver framework supports both cases using boundary conditions.

---

## 5. Numerical Stability Considerations

To ensure stability:
- Force relaxation is applied:
  F_applied = α F_new + (1 − α) F_old
- Typical relaxation factor:
  α = 0.2 – 0.5

Optional sub-iterations can be enabled for strong coupling cases.

---

## 6. Software Architecture Mapping

Each module corresponds to an independent software component:

- wind_solver/
- wave_solver/
- structure_solver/
- solar_solver/
- coupling_manager/

The coupling manager controls:
- Time stepping
- Data transfer
- Logging and output

---

## 7. Extensibility

Future extensions:
- Array-scale wind farm interaction
- Wave energy converter coupling
- Electrical
