syms E_x E_y E_z B_x B_y B_z Q_enc I_enc t

% Define electric field vector
E = [E_x, E_y, E_z];

% Define magnetic field vector
B = [B_x, B_y, B_z];

% Define surface area vector
dA = [da_x, da_y, da_z];

% Define line element vector
dl = [dl_x, dl_y, dl_z];

% Define charge density
rho = Q_enc / dV;

% Define current density
J = I_enc / dA;

% Define vacuum permittivity and permeability
epsilon_0 = 8.85418782e-12;
mu_0 = 1.25663706e-6;

% Calculate integral form of Maxwell's equations
eq1 = int(E*dA) == Q_enc / epsilon_0;
eq2 = int(E*dl) == -int(diff(B,t)*dA);
eq3 = int(B*dA) == 0;
eq4 = int(B*dl) == mu_0*I_enc + mu_0*epsilon_0*int(diff(E,t)*dA);
