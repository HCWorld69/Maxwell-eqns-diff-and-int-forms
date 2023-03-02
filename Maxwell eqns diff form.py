syms x y z t
syms rho Q_enc I_enc
syms epsilon_0 mu_0
E = sym('E', [3, 1]);
B = sym('B', [3, 1]);
J = sym('J', [3, 1]);

% Differential form of Maxwell's equations
eq1 = divergence(E) == rho/epsilon_0;
eq2 = curl(E) == -diff(B, t);
eq3 = divergence(B) == 0;
eq4 = curl(B) == mu_0*J + mu_0*epsilon_0*diff(E, t);
