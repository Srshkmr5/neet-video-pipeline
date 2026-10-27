import json

with open('apps/curriculum_manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

unit3_data = [
    {
        'canonical_id': 'P11-C03-T01-V01',
        'title': 'First Law of Motion, Inertia and Free-Body Diagrams',
        'latex_formula': r'\sum \vec{F}_{\text{ext}} = 0 \implies \vec{a} = 0',
        'plain_formula': 'F_net = 0 => a = 0 (Equilibrium)',
        'ncert_citation': 'NCERT Class 11 Physics, Chapter 4, Sec 4.2 - 4.3',
        'ncert_core_rule': 'A body continues in its state of rest or uniform motion in a straight line unless acted upon by a non-zero net external force. Free-Body Diagrams isolate the body and show ONLY forces acting ON the body by the surroundings.',
        'author_book_nuance': 'Internal forces cancel out in action-reaction pairs; only external forces can accelerate the system.',
        'neet_trap_point': 'Never include internal forces or forces exerted BY the body on other objects in its own FBD.',
        'pyq_years': 'NEET 2021, 2017',
        'simulation': '/simulations/unit_03_laws_of_motion_lab.html?concept=P11-C03-T01-V01',
        'trap_quiz': {
            'title': 'NEET Trap: Free-Body Diagram Construction',
            'warning': 'Including forces exerted BY the body in its own FBD.',
            'pyq_year': 'NEET 2021',
            'formula_card': {
                'incorrect': 'F_FBD = F_on_body + F_by_body',
                'correct': 'F_FBD = Σ F_external_on_body'
            },
            'question': 'When drawing the Free-Body Diagram (FBD) of a horse pulling a cart accelerating forward, which of the following horizontal forces must be included on the HORSE?',
            'options': [
                {'id': 0, 'text': 'A) Forward friction from the ground on the horse and backward tension from the cart.', 'trap': 'Correct: Only external forces acting ON the horse are drawn.', 'correct': True},
                {'id': 1, 'text': 'B) Forward force exerted by the horse on the cart and backward friction.', 'trap': 'Trap: Force on cart acts on CART, not on the horse.'},
                {'id': 2, 'text': 'C) Backward pull by the cart and the horse internal muscular force.', 'trap': 'Trap: Internal muscular forces never appear in an external FBD.'},
                {'id': 3, 'text': 'D) Normal force from the cart and gravity only.', 'trap': 'Trap: Misses horizontal ground friction which propels the system forward.'}
            ],
            'correct_index': 0,
            'explanation': 'An FBD must include strictly external forces acting ON the chosen body: forward static friction from ground on horse, and backward tension from cart.'
        }
    },
    {
        'canonical_id': 'P11-C03-T01-V02',
        'title': 'Second Law of Motion, Elevators and Pseudo Forces',
        'latex_formula': r'\vec{F}_{\text{net}} = \frac{d\vec{p}}{dt} = m\vec{a}, \quad N_{\text{app}} = m(g \pm a)',
        'plain_formula': 'F_net = m*a, N_app = m(g +/- a)',
        'ncert_citation': 'NCERT Class 11 Physics, Chapter 4, Sec 4.4',
        'ncert_core_rule': 'In an accelerating frame with acceleration a_0, a fictitious pseudo force F_pseudo = -m*a_0 acts opposite to frame acceleration. Apparent weight in elevator: N = m(g+a) for upward acceleration, N = m(g-a) for downward acceleration.',
        'author_book_nuance': 'Velocity direction does not matter; only the direction of acceleration determines apparent weight.',
        'neet_trap_point': 'Confusing upward velocity with upward acceleration. An elevator moving upwards but slowing down has a downwards, so N = m(g - a)!',
        'pyq_years': 'NEET 2023, 2020, 2018',
        'simulation': '/simulations/unit_03_laws_of_motion_lab.html?concept=P11-C03-T01-V02',
        'trap_quiz': {
            'title': 'NEET Trap: Elevator Apparent Weight vs Direction of Motion',
            'warning': 'Assuming upward motion always implies increased apparent weight.',
            'pyq_year': 'NEET 2023',
            'formula_card': {
                'incorrect': 'Moving Upwards => N = m(g + a)',
                'correct': 'Accelerating Upwards => N = m(g + a); Decelerating Upwards => N = m(g - a)'
            },
            'question': 'A man of mass 70 kg stands on a weighing scale in an elevator moving UPWARDS but SLOWING DOWN at 2 m/s². What does the scale read? (g = 10 m/s²)',
            'options': [
                {'id': 0, 'text': 'A) 560 N (56 kg)', 'trap': 'Correct: Upward velocity with deceleration means acceleration is DOWNWARD: N = m(g - a) = 70*(10-2) = 560 N.', 'correct': True},
                {'id': 1, 'text': 'B) 840 N (84 kg)', 'trap': 'Trap: Inverted acceleration direction assuming moving up means adding a.'},
                {'id': 2, 'text': 'C) 700 N (70 kg)', 'trap': 'Trap: Ignored elevator deceleration.'},
                {'id': 3, 'text': 'D) 140 N (14 kg)', 'trap': 'Trap: Calculated m*a instead of Normal reaction m(g - a).'}
            ],
            'correct_index': 0,
            'explanation': 'Slowing down while moving upwards means net acceleration is directed downwards. Hence N = m(g - a) = 70*(10 - 2) = 560 N.'
        }
    },
    {
        'canonical_id': 'P11-C03-T01-V03',
        'title': 'Third Law of Motion, Action-Reaction and String Tension',
        'latex_formula': r'\vec{F}_{AB} = -\vec{F}_{BA}, \quad T = \frac{2m_1 m_2}{m_1 + m_2}g',
        'plain_formula': 'F_AB = -F_BA, T = 2*m1*m2*g / (m1 + m2)',
        'ncert_citation': 'NCERT Class 11 Physics, Chapter 4, Sec 4.5',
        'ncert_core_rule': 'Action and reaction act on two different bodies simultaneously; they never cancel each other on a single body. In a light inextensible string passing over a frictionless pulley, tension is uniform throughout.',
        'author_book_nuance': 'Normal force and gravity on a resting book are NOT action-reaction pairs.',
        'neet_trap_point': 'Assuming Normal force and gravity cancel because of Newton Third Law; they balance because of the First Law (equilibrium on a single body)!',
        'pyq_years': 'NEET 2022, 2019, 2016',
        'simulation': '/simulations/unit_03_laws_of_motion_lab.html?concept=P11-C03-T01-V03',
        'trap_quiz': {
            'title': 'NEET Trap: Action-Reaction vs Equilibrium Forces',
            'warning': 'Confusing balanced forces on one object with Newton Third Law pairs.',
            'pyq_year': 'NEET 2022',
            'formula_card': {
                'incorrect': 'N = mg constitutes an Action-Reaction Pair',
                'correct': 'N and mg act on SAME body (Equilibrium); Action-Reaction acts on TWO different bodies'
            },
            'question': 'A book rests on a table. The normal reaction force exerted by the table on the book is N, and gravitational pull on the book is W = mg. What is the reaction force to the weight W?',
            'options': [
                {'id': 0, 'text': 'A) Gravitational upward attraction exerted by the book on the Earth.', 'trap': 'Correct: Earth pulls book down, so book pulls Earth up (Newton 3rd Law pair).', 'correct': True},
                {'id': 1, 'text': 'B) The normal upward reaction force N of the table on the book.', 'trap': 'Trap: Table force is contact force, not the gravitational reaction partner.'},
                {'id': 2, 'text': 'C) The downward pressure exerted by the book on the table.', 'trap': 'Trap: That is the reaction to the table normal force, not gravity.'},
                {'id': 3, 'text': 'D) Zero, because the book is in static rest.', 'trap': 'Trap: Action-reaction pairs exist universally regardless of motion state.'}
            ],
            'correct_index': 0,
            'explanation': 'Weight is the Earth pulling the book down. By Newton 3rd Law, the reaction partner is the book pulling the Earth upwards with equal gravitational magnitude.'
        }
    },
    {
        'canonical_id': 'P11-C03-T02-V04',
        'title': 'Linear Momentum, Impulse and Area under F-t Curve',
        'latex_formula': r'\vec{J} = \int_{t_1}^{t_2} \vec{F} \, dt = \Delta \vec{p} = m(\vec{v}_f - \vec{v}_i)',
        'plain_formula': 'J = F_avg * dt = Delta p = Area(F-t curve)',
        'ncert_citation': 'NCERT Class 11 Physics, Chapter 4, Sec 4.4.1',
        'ncert_core_rule': 'Impulse equals change in linear momentum. Area under the Force-Time curve gives total impulse. In an elastic wall collision with rebound, delta p = m*v - (-m*v) = 2*m*v.',
        'author_book_nuance': 'Momentum is a vector quantity; sign inversion upon reversal doubles the change in momentum.',
        'neet_trap_point': 'Forgetting the negative sign of rebound velocity, calculating Delta p = mv - mv = 0 instead of 2mv.',
        'pyq_years': 'NEET 2024, 2021, 2019',
        'simulation': '/simulations/unit_03_laws_of_motion_lab.html?concept=P11-C03-T02-V04',
        'trap_quiz': {
            'title': 'NEET Trap: Rebound Impulse Vector Sign Inversion',
            'warning': 'Subtracting magnitudes instead of vector velocities during rebound.',
            'pyq_year': 'NEET 2024',
            'formula_card': {
                'incorrect': 'Rebound Δp = m·v - m·v = 0',
                'correct': 'Rebound Δp = m·v - (-m·v) = 2m·v'
            },
            'question': 'A ball of mass 0.2 kg moving horizontally at 15 m/s strikes a hard vertical wall and rebounds elastically at the same speed. Contact lasts 0.01 s. What is the average force exerted on the wall?',
            'options': [
                {'id': 0, 'text': 'A) 600 N', 'trap': 'Correct: Δp = m*(15 - (-15)) = 0.2*30 = 6 kg·m/s. F_avg = Δp / Δt = 6 / 0.01 = 600 N.', 'correct': True},
                {'id': 1, 'text': 'B) 300 N', 'trap': 'Trap: Forgot the rebound doubling, calculating only m*v / Δt.'},
                {'id': 2, 'text': 'C) 0 N', 'trap': 'Trap: Subtracted equal speeds without accounting for opposite direction vectors.'},
                {'id': 3, 'text': 'D) 150 N', 'trap': 'Trap: Arithmetic calculation error.'}
            ],
            'correct_index': 0,
            'explanation': 'Because the ball rebounds in the opposite direction, Δv = 15 - (-15) = 30 m/s. Impulse = 0.2 * 30 = 6 N·s. Force = 6 / 0.01 = 600 N.'
        }
    },
    {
        'canonical_id': 'P11-C03-T02-V05',
        'title': 'Conservation of Linear Momentum and Rocket Thrust',
        'latex_formula': r'\sum \vec{p}_i = \sum \vec{p}_f, \quad F_{\text{thrust}} = v_{\text{rel}}\left(-\frac{dm}{dt}\right)',
        'plain_formula': 'p_initial = p_final, v_recoil = -(m/M)*v_bullet, F_thrust = v_rel * |dm/dt|',
        'ncert_citation': 'NCERT Class 11 Physics, Chapter 4, Sec 4.6',
        'ncert_core_rule': 'In the absence of net external force, total linear momentum remains constant. Recoil velocity of rifle is V = -(m/M)*v. Rocket thrust depends on exhaust velocity and rate of fuel consumption.',
        'author_book_nuance': 'Momentum is conserved along each Cartesian coordinate independently (x, y, z).',
        'neet_trap_point': 'Neglecting the mass of the bullet when computing total rifle+bullet mass after firing or using scalar speeds.',
        'pyq_years': 'NEET 2022, 2018, 2015',
        'simulation': '/simulations/unit_03_laws_of_motion_lab.html?concept=P11-C03-T02-V05',
        'trap_quiz': {
            'title': 'NEET Trap: Variable Mass Rocket Acceleration',
            'warning': 'Forgetting that rocket mass decreases continuously as fuel burns.',
            'pyq_year': 'NEET 2022',
            'formula_card': {
                'incorrect': 'a_rocket = F_thrust / M_initial (constant)',
                'correct': 'a_rocket(t) = F_thrust / M(t) - g (increases as mass burns away)'
            },
            'question': 'A rocket of total initial mass 6000 kg ejects exhaust gas at a constant relative speed of 1000 m/s at a rate of 60 kg/s. If g = 10 m/s², what is the initial net acceleration of the rocket at blast-off?',
            'options': [
                {'id': 0, 'text': 'A) 0 m/s² (Thrust exactly balances initial weight)', 'trap': 'Correct: F_thrust = v_rel*(dm/dt) = 1000*60 = 60,000 N. Weight W = 6000*10 = 60,000 N. Net F = 0, so initial a = 0.', 'correct': True},
                {'id': 1, 'text': 'B) 10 m/s²', 'trap': 'Trap: Forgot to subtract gravity pull.'},
                {'id': 2, 'text': 'C) 20 m/s²', 'trap': 'Trap: Added gravity instead of opposing thrust.'},
                {'id': 3, 'text': 'D) 5 m/s²', 'trap': 'Trap: Incorrect mass ratio computation.'}
            ],
            'correct_index': 0,
            'explanation': 'Thrust = 1000 * 60 = 60,000 N. Weight = 6000 * 10 = 60,000 N. Net upward force = 0 N, so initial net acceleration is 0 m/s² (just hovering at launch).'
        }
    },
    {
        'canonical_id': 'P11-C03-T02-V06',
        'title': "Equilibrium of Concurrent Forces and Lami's Theorem",
        'latex_formula': r'\frac{F_1}{\sin\alpha} = \frac{F_2}{\sin\beta} = \frac{F_3}{\sin\gamma}, \quad \sum \vec{F} = 0',
        'plain_formula': 'F1/sin(alpha) = F2/sin(beta) = F3/sin(gamma)',
        'ncert_citation': 'NCERT Class 11 Physics, Chapter 4, Sec 4.7',
        'ncert_core_rule': 'When three coplanar concurrent forces act on a body in equilibrium, each force is proportional to the sine of the angle between the remaining two forces.',
        'author_book_nuance': 'Forces must act at the same single point (concurrent); Lami\'s theorem cannot be used for rotational equilibrium.',
        'neet_trap_point': 'Taking the angle between the force and an axis rather than the interior angle between the other two forces.',
        'pyq_years': 'NEET 2023, 2020',
        'simulation': '/simulations/unit_03_laws_of_motion_lab.html?concept=P11-C03-T02-V06',
        'trap_quiz': {
            'title': "NEET Trap: Lami's Theorem Angle Association",
            'warning': 'Using angles with axes instead of opposite force pair angles.',
            'pyq_year': 'NEET 2023',
            'formula_card': {
                'incorrect': 'F_1 / sin(angle_with_x_axis) = F_2 / sin(...)',
                'correct': 'F_1 / sin(θ between F_2 and F_3) = F_2 / sin(θ between F_1 and F_3)'
            },
            'question': 'A weight W = 100 N is suspended by two strings of equal length attached to a ceiling, making 60° with each other at the knot. By symmetry and Lami theorem, what is the tension in each string?',
            'options': [
                {'id': 0, 'text': 'A) 57.7 N (100 / √3 N)', 'trap': 'Correct: Angle between vertical W and each string is 150°. T / sin(150°) = W / sin(60°) => T = 100 * (0.5 / (√3/2)) = 100/√3 ≈ 57.7 N.', 'correct': True},
                {'id': 1, 'text': 'B) 100 N', 'trap': 'Trap: Ignored angle splitting.'},
                {'id': 2, 'text': 'C) 50 N', 'trap': 'Trap: Assumed 2T = W without cosine factor.'},
                {'id': 3, 'text': 'D) 86.6 N', 'trap': 'Trap: Used cos(60°) instead of vertical resolving angle 30°.'}
            ],
            'correct_index': 0,
            'explanation': 'Angle between strings is 60°, so each string is at 30° to the vertical. 2*T*cos(30°) = W => 2*T*(√3/2) = 100 => T = 100/√3 ≈ 57.7 N.'
        }
    },
    {
        'canonical_id': 'P11-C03-T03-V07',
        'title': 'Static vs Kinetic Friction, Limiting Value and Graphs',
        'latex_formula': r'f_s \le \mu_s N, \quad f_{s,\max} = \mu_s N, \quad f_k = \mu_k N \quad (\mu_k < \mu_s)',
        'plain_formula': 'f_s <= mu_s * N, f_k = mu_k * N',
        'ncert_citation': 'NCERT Class 11 Physics, Chapter 4, Sec 4.8',
        'ncert_core_rule': 'Static friction is self-adjusting (fs = F_applied) up to the limiting threshold mu_s * N. Once relative motion begins, friction drops slightly to kinetic friction f_k = mu_k * N and stays constant.',
        'author_book_nuance': 'Friction opposes relative motion between surfaces in contact, NOT necessarily absolute motion.',
        'neet_trap_point': 'Assuming static friction is always equal to mu_s * N even when applied force is small.',
        'pyq_years': 'NEET 2024, 2021, 2017',
        'simulation': '/simulations/unit_03_laws_of_motion_lab.html?concept=P11-C03-T03-V07',
        'trap_quiz': {
            'title': 'NEET Trap: Static Friction Self-Adjusting Property',
            'warning': 'Assuming static friction is always equal to its maximum limiting value μ_s·N.',
            'pyq_year': 'NEET 2024',
            'formula_card': {
                'incorrect': 'f_static = μ_s·N (always)',
                'correct': 'f_static = F_applied (when F_applied < μ_s·N); f_s,max = μ_s·N'
            },
            'question': 'A block of mass 5 kg rests on a rough horizontal floor with μ_s = 0.6 and μ_k = 0.4. A horizontal force of 15 N is applied to the block. (g = 10 m/s²). What is the frictional force acting on the block?',
            'options': [
                {'id': 0, 'text': 'A) 15 N', 'trap': 'Correct: Limiting friction f_max = 0.6*50 = 30 N. Since F_app = 15 N < 30 N, block remains static, so friction equals applied force: f = 15 N.', 'correct': True},
                {'id': 1, 'text': 'B) 30 N', 'trap': 'Trap: Blindly substituted f = μ_s*N.'},
                {'id': 2, 'text': 'C) 20 N', 'trap': 'Trap: Assumed kinetic friction f_k = μ_k*N even though block does not move.'},
                {'id': 3, 'text': 'D) 0 N', 'trap': 'Trap: Assumed zero friction because block is stationary.'}
            ],
            'correct_index': 0,
            'explanation': 'Limiting friction is f_s,max = 0.6 * 50 = 30 N. Because applied force (15 N) is less than 30 N, static friction self-adjusts to exactly 15 N to maintain equilibrium.'
        }
    },
    {
        'canonical_id': 'P11-C03-T03-V08',
        'title': 'Rough Inclined Plane, Angle of Repose and Acceleration',
        'latex_formula': r'\tan\theta_R = \mu_s, \quad a_{\text{down}} = g(\sin\theta - \mu_k\cos\theta), \quad a_{\text{up}} = g(\sin\theta + \mu_k\cos\theta)',
        'plain_formula': 'tan(theta_repose) = mu_s, a_down = g(sin theta - mu_k * cos theta)',
        'ncert_citation': 'NCERT Class 11 Physics, Chapter 4, Sec 4.8.1',
        'ncert_core_rule': 'Angle of Repose theta_R is the minimum tilt angle where a block begins to slide on its own (tan theta_R = mu_s). When sliding down, friction opposes motion upwards, so a = g(sin theta - mu_k*cos theta). Sliding up, friction opposes motion downwards, so a = g(sin theta + mu_k*cos theta).',
        'author_book_nuance': 'Because upward deceleration is greater than downward acceleration, time of ascent is strictly less than time of descent on a rough incline.',
        'neet_trap_point': 'Using the same acceleration for upward and downward motion on a rough incline.',
        'pyq_years': 'NEET 2023, 2020, 2016',
        'simulation': '/simulations/unit_03_laws_of_motion_lab.html?concept=P11-C03-T03-V08',
        'trap_quiz': {
            'title': 'NEET Trap: Ascent vs Descent Time on Rough Incline',
            'warning': 'Assuming time to go up equals time to slide down on a rough plane.',
            'pyq_year': 'NEET 2023',
            'formula_card': {
                'incorrect': 't_ascent = t_descent on rough incline',
                'correct': 'a_up = g(sinθ + μcosθ) > a_down = g(sinθ - μcosθ) => t_descent > t_ascent'
            },
            'question': 'A block is projected up an incline of angle θ with friction coefficient μ. Which statement correctly relates the time of ascent (t_up) and time of descent (t_down)?',
            'options': [
                {'id': 0, 'text': 'A) t_down > t_up, because downward acceleration is smaller due to upward friction.', 'trap': 'Correct: a_down = g(sinθ - μcosθ) < a_up = g(sinθ + μcosθ). With smaller acceleration, downward time is longer.', 'correct': True},
                {'id': 1, 'text': 'B) t_down = t_up, by kinematic symmetry.', 'trap': 'Trap: Symmetry holds only for frictionless inclines!'},
                {'id': 2, 'text': 'C) t_up > t_down, because gravity assists going down.', 'trap': 'Trap: Friction opposes motion in both directions, making downward net acceleration smaller.'},
                {'id': 3, 'text': 'D) Depends on the mass of the block.', 'trap': 'Trap: Mass cancels out completely in incline equations.'}
            ],
            'correct_index': 0,
            'explanation': 'Going up, gravity and friction both act downwards: a_up = g(sinθ + μcosθ). Going down, friction acts upwards: a_down = g(sinθ - μcosθ). Smaller acceleration over the same distance means t_down > t_up.'
        }
    },
    {
        'canonical_id': 'P11-C03-T03-V09',
        'title': 'Two-Block Friction Systems and Relative Motion Threshold',
        'latex_formula': r'a_{\max} = \mu_s g, \quad F_{\max} = (m_1 + m_2)\mu_s g',
        'plain_formula': 'a_max = mu_s * g, F_max = (m1 + m2) * mu_s * g',
        'ncert_citation': 'NCERT Class 11 Physics, Chapter 4, Sec 4.8.2',
        'ncert_core_rule': 'When block m1 rests atop m2, the only horizontal force accelerating m1 is friction between the two blocks. Maximum common acceleration is a_max = mu_s*g. For applied force F > F_max, slipping occurs and friction becomes kinetic.',
        'author_book_nuance': 'Identify which block is driven by friction alone; that block limiting friction dictates the maximum acceleration without slipping.',
        'neet_trap_point': 'Assuming both blocks accelerate together regardless of how large the pulling force is.',
        'pyq_years': 'NEET 2022, 2019, 2018',
        'simulation': '/simulations/unit_03_laws_of_motion_lab.html?concept=P11-C03-T03-V09',
        'trap_quiz': {
            'title': 'NEET Trap: Two-Block Relative Slipping Threshold',
            'warning': 'Assuming two stacked blocks always accelerate as a single combined mass.',
            'pyq_year': 'NEET 2022',
            'formula_card': {
                'incorrect': 'a_common = F / (m1 + m2) for any applied force F',
                'correct': 'a_common applies only if F ≤ (m1 + m2)·μ_s·g; else slipping occurs'
            },
            'question': 'Block A of mass 2 kg sits on top of Block B of mass 4 kg resting on a frictionless floor. Coefficient of static friction between A and B is μ_s = 0.4. What is the maximum horizontal force applied to B so that A does not slip on B? (g = 10 m/s²)',
            'options': [
                {'id': 0, 'text': 'A) 24 N', 'trap': 'Correct: Max acceleration of A is a_max = μ_s*g = 0.4*10 = 4 m/s². Maximum force on system: F_max = (m_A + m_B)*a_max = (2 + 4)*4 = 24 N.', 'correct': True},
                {'id': 1, 'text': 'B) 8 N', 'trap': 'Trap: Calculated only limiting friction on A (0.4*20 = 8 N) without multiplying total system mass.'},
                {'id': 2, 'text': 'C) 16 N', 'trap': 'Trap: Applied acceleration to block B alone.'},
                {'id': 3, 'text': 'D) 40 N', 'trap': 'Trap: Arithmetic calculation error.'}
            ],
            'correct_index': 0,
            'explanation': 'Friction accelerates Block A: f_max = μ_s * m_A * g = 0.4 * 2 * 10 = 8 N. Max common acceleration a_max = f_max / m_A = 4 m/s². Total force on both blocks: F_max = (m_A + m_B) * a_max = 6 * 4 = 24 N.'
        }
    },
    {
        'canonical_id': 'P11-C03-T04-V10',
        'title': 'Centripetal Force and Level Curved Road Dynamics',
        'latex_formula': r'F_c = \frac{m v^2}{r} = m \omega^2 r, \quad v_{\max} = \sqrt{\mu_s r g}',
        'plain_formula': 'F_c = m*v^2 / r, v_max = sqrt(mu_s * r * g)',
        'ncert_citation': 'NCERT Class 11 Physics, Chapter 4, Sec 4.9',
        'ncert_core_rule': 'On a level unbanked curved road, static friction between tires and road provides the entire centripetal force. The maximum safe speed without skidding is v_max = sqrt(mu_s * r * g), completely independent of car mass.',
        'author_book_nuance': 'It is static friction that prevents skidding; if tires start skidding, kinetic friction takes over, drastically reducing steering control.',
        'neet_trap_point': 'Assuming heavier vehicles have higher maximum turn speed on a level road. Mass cancels out!',
        'pyq_years': 'NEET 2024, 2022, 2019',
        'simulation': '/simulations/unit_03_laws_of_motion_lab.html?concept=P11-C03-T04-V10',
        'trap_quiz': {
            'title': 'NEET Trap: Mass Independence on Level Road Turns',
            'warning': 'Believing a heavier vehicle can take a flat turn faster due to higher normal force.',
            'pyq_year': 'NEET 2024',
            'formula_card': {
                'incorrect': 'Heavy Truck v_max > Small Car v_max on flat curve',
                'correct': 'v_max = √(μ_s·r·g) — Strictly independent of mass m'
            },
            'question': 'A sports car of mass 1000 kg and a loaded truck of mass 5000 kg negotiate the same unbanked circular curve of radius 50 m on a road with μ_s = 0.5. How do their maximum safe speeds compare?',
            'options': [
                {'id': 0, 'text': 'A) Both have the exact same maximum safe speed (v_max = 15.8 m/s).', 'trap': 'Correct: v_max = √(μ_s * r * g) = √(0.5 * 50 * 10) = 15.8 m/s, strictly independent of vehicle mass.', 'correct': True},
                {'id': 1, 'text': 'B) The truck can turn faster because its greater weight provides more friction.', 'trap': 'Trap: Higher normal force also requires proportionally more centripetal force (m cancels).'},
                {'id': 2, 'text': 'C) The car can turn 5 times faster because it is lighter.', 'trap': 'Trap: Mass does not favor either vehicle for maximum skidding speed.'},
                {'id': 3, 'text': 'D) Truck requires a banked road, car does not.', 'trap': 'Trap: Both obey identical friction dynamics on a flat road.'}
            ],
            'correct_index': 0,
            'explanation': 'Centripetal force is provided by static friction: m*v²/r = μ_s*m*g => v_max = √(μ_s * r * g). Mass m cancels out on both sides, so both vehicles have the identical safe limit.'
        }
    },
    {
        'canonical_id': 'P11-C03-T04-V11',
        'title': 'Engineered Banking of Roads and Vertical Circles',
        'latex_formula': r'v_0 = \sqrt{r g \tan\theta}, \quad v_{\max} = \sqrt{\frac{rg(\tan\theta + \mu_s)}{1 - \mu_s\tan\theta}}, \quad v_{\text{bottom}} \ge \sqrt{5gr}',
        'plain_formula': 'v_opt = sqrt(r*g*tan theta), v_bottom >= sqrt(5*g*r) for vertical loop',
        'ncert_citation': 'NCERT Class 11 Physics, Chapter 4, Sec 4.9.1',
        'ncert_core_rule': 'Banking raises the outer edge so the horizontal component of Normal reaction N*sin theta provides centripetal force without relying on friction (optimum speed v_0 = sqrt(r*g*tan theta)). For a vertical circle on a string, minimum speed to loop is sqrt(5gr) at bottom and sqrt(gr) at apex.',
        'author_book_nuance': 'For a light rigid rod, speed at apex can reach 0, so v_bottom >= sqrt(4gr) = 2*sqrt(gr), whereas a string goes slack unless v_apex >= sqrt(gr).',
        'neet_trap_point': 'Confusing string looping condition (v >= sqrt(5gr)) with light rigid rod condition (v >= sqrt(4gr) = 2sqrt(gr)).',
        'pyq_years': 'NEET 2023, 2020, 2017',
        'simulation': '/simulations/unit_03_laws_of_motion_lab.html?concept=P11-C03-T04-V11',
        'trap_quiz': {
            'title': 'NEET Trap: String vs Rigid Rod in Vertical Circle Looping',
            'warning': 'Using string velocity threshold v_bottom = √(5gl) for a rigid rod.',
            'pyq_year': 'NEET 2023',
            'formula_card': {
                'incorrect': 'Rigid Rod Loop v_bottom = √(5g·l)',
                'correct': 'String: v_top ≥ √(g·l) => v_bot ≥ √(5g·l); Rigid Rod: v_top ≥ 0 => v_bot ≥ √(4g·l) = 2√(g·l)'
            },
            'question': 'A small sphere is attached to a light RIGID rod of length L and whirled in a vertical circle. What is the minimum speed at the lowest point so that the sphere completes a full vertical loop?',
            'options': [
                {'id': 0, 'text': 'A) √(4gL) = 2√(gL)', 'trap': 'Correct: A rigid rod can support compression, so velocity at the top can be zero without going slack. Energy conservation: 0.5*m*v² = m*g*(2L) => v = √(4gL).', 'correct': True},
                {'id': 1, 'text': 'B) √(5gL)', 'trap': 'Trap: That is for a flexible string where tension must be ≥ 0 at the top!'},
                {'id': 2, 'text': 'C) √(2gL)', 'trap': 'Trap: That only brings the sphere to the horizontal position, not the top.'},
                {'id': 3, 'text': 'D) √(6gL)', 'trap': 'Trap: Overestimated energy requirement.'}
            ],
            'correct_index': 0,
            'explanation': 'Unlike a string which becomes slack unless v_top ≥ √(gL), a rigid rod cannot slacken. The sphere only needs to reach the apex with v_top = 0. By energy conservation: 0.5*m*v_bot² = m*g*(2L) => v_bot = √(4gL) = 2√(gL).'
        }
    }
]

id_map = {item['canonical_id']: item for item in unit3_data}
updated_count = 0
for i, c in enumerate(manifest['concepts']):
    cid = c.get('canonical_id')
    if cid in id_map:
        data = id_map[cid]
        c['title'] = data['title']
        c['latex_formula'] = data['latex_formula']
        c['plain_formula'] = data['plain_formula']
        c['ncert_citation'] = data['ncert_citation']
        c['ncert_core_rule'] = data['ncert_core_rule']
        c['author_book_nuance'] = data['author_book_nuance']
        c['neet_trap_point'] = data['neet_trap_point']
        c['pyq_years'] = data['pyq_years']
        c['simulation'] = data['simulation']
        c['trap_quiz'] = data['trap_quiz']
        updated_count += 1

with open('apps/curriculum_manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f'Successfully updated {updated_count}/11 Unit 3 concepts in curriculum_manifest.json!')
