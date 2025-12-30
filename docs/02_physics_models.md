# Physics Models

This document describes the physical and mathematical models used in the
Offshore Hybrid Energy Platform. The modeling approach prioritizes
**physical consistency, numerical stability, and buildability**
over excessive complexity.

The platform integrates wind, wave, and solar energy systems
through a shared offshore structure (fixed or floating).

----

## 1. Wind Field Model

### 1.1 Governing Equations

The wind field is modeled using the **3D incompressible Reynolds-Averaged
Navier–Stokes (RANS) equations**:

Continuity:
∇ · u = 0

Momentum:
∂u/∂t + (u · ∇)u =
− (1/ρ) ∇p + ∇ · [(ν + ν_t) ∇u] + F_turbine

where:
- u : velocity vector
- p : pressure
- ρ : air density
- ν : kinematic viscosity
- ν_t : turbulent eddy viscosity
- F_turbine : turbine-induced body force

---

### 1.2 Turbulence Modeling

The baseline turbulence model is:
- **k–ε model** (robust and computationally efficient)

Advanced option:
- **k–ω SST model** for improved wake and near-wall behavior

---

### 1.3 Wind Turbine Representation

#### Actuator Disk Model (ADM)

The turbine is represented as a distributed momentum sink:

F_x = − ½ ρ C_T U² A

where:
- C_T : thrust coefficient
- U : local disk-averaged velocity
- A : rotor swept area

The force is smoothly distributed over the disk volume.

#### Actuator Line Model (ALM) (future extension)

Blade Element Momentum (BEM) theory is used:

Lift:
L = ½ ρ C_L c U_rel²

Drag:
D = ½ ρ C_D c U_rel²

This approach avoids moving meshes and allows blade-level force resolution.

---

## 2. Wave and Current Model

### 2.1 Wave Representation

Waves are modeled using:
- Linear wave theory
- Spectral representation (JONSWAP spectrum)

Free surface elevation:
η(t) = Σ a_i cos(ω_i t + φ_i)

where:
- a_i : wave amplitude
- ω_i : angular frequency
- φ_i : random phase

---

### 2.2 Hydrodynamic Loading

Wave-induced forces on structural elements are computed using the
**Morison equation**:

F = ρ C_m V (du/dt) + ½ ρ C_d A |u| u

where:
- C_m : inertia coefficient
- C_d : drag coefficient
- u : water particle velocity

This formulation is applicable to both fixed and floating structures.

---

## 3. Platform Dynamics

### 3.1 Rigid Body Motion (6 DOF)

The offshore platform motion is modeled using a rigid-body formulation:

M x¨ + C x˙ + K x =
F_wind + F_wave + F_current + F_mooring

Degrees of freedom:
- Surge, sway, heave
- Roll, pitch, yaw

where:
- M : mass and added mass matrix
- C : damping matrix
- K : hydrostatic restoring matrix

---

### 3.2 Fixed-Bottom Case

For fixed-bottom structures:
- Platform motion is constrained
- Structural response is evaluated through force and stress outputs

This allows a single framework to support both fixed and floating systems.

---

## 4. Mooring and Foundation Models

### 4.1 Mooring System (Floating)

- Quasi-static catenary formulation
- Linearized stiffness matrix

Mooring force:
F_mooring = − K_m x

---

### 4.2 Foundation Model (Fixed)

- Soil–structure interaction represented by spring–dashpot elements
- Effective stiffness calibrated from geotechnical parameters

---

## 5. Solar Energy Model

Floating solar panels are modeled using
