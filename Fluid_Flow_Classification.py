import numpy as np

def calculate_reynolds_number(density, velocity, diameter, viscosity):
  """Calculates the Reynolds number for a fluid flow.

  Args:
    density: Density of the fluid (kg/m^3)
    velocity: Velocity of the fluid (m/s)
    diameter: Diameter of the pipe (m)
    viscosity: Dynamic viscosity of the fluid (Pa*s)

  Returns:
    Reynolds number (dimensionless)
  """

  reynolds_number = (density * velocity * diameter) / viscosity
  return reynolds_number

def classify_flow(reynolds_number):
  """Classifies the fluid flow based on Reynolds number.

  Args:
    reynolds_number: The calculated Reynolds number.

  Returns:
    A string indicating the flow regime (laminar, transitional, or turbulent)
  """

  if reynolds_number <= 2100:
    return "Laminar"
  elif 2100 < reynolds_number < 4000:
    return "Transitional"
  else: reynolds_number >= 4000
  return "Turbulent"

def main():
  density = float(input("Enter fluid density (kg/m^3): "))
  velocity = float(input("Enter fluid velocity (m/s): "))
  diameter = float(input("Enter pipe diameter (m): "))
  viscosity = float(input("Enter fluid viscosity (Pa*s): "))

  re = calculate_reynolds_number(density, velocity, diameter, viscosity)
  flow_regime = classify_flow(re)

  print("Reynolds number:", re)
  print("Flow regime:", flow_regime)

if __name__ == "__main__":
  main()