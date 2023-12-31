import random
import matplotlib.pyplot as plt
def distance_matrix_reader(file_path):
    cities_distance_list = []  
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = lines[2:32]
        for line in lines:
            city = [int(num) for num in line.strip().split()]
            cities_distance_list.append(city)
    return cities_distance_list
######################################### class for build trips ######################################################################
class Country:
    def __init__(self,trips_number,cities_number=30):
        self.cities_number=cities_number
        self.trips_number=trips_number
        self.trips=[]
        self.trips = [random.sample(range(cities_number), cities_number) for _ in range(trips_number)]
######################################### class for TSP Algorithms and their functions ######################################################################
class TSP:
    def __init__(self, population, dist_matrix):
        self.population = population
        self.dist_matrix = dist_matrix
        self.fitness_population = {}
        self.save_bwindividual={}
    ######################## function for evaluate fitness of each individual in population #######################################
    def fitness(self):
        self.fitness_population = {}
        for i, path in enumerate(self.population):
            distances = [self.dist_matrix[path[j]][path[(j + 1) % len(path)]] for j in range(len(path))]
            fitness_value = sum(distances)
            self.fitness_population[i] = fitness_value
        return self.fitness_population

    ######################## function for implement tournoment selection #######################################
    def tournament_selection(self):
        parents = sorted(set(random.choices(self.fitness_population, k=5)))
        
        for key,value in self.fitness_population.items():
            if value==parents[0]:
                first_parent=key
            if value==parents[1]:
                second_parent=key
        
        return first_parent,second_parent
    ######################## function for PMX crossover #######################################
    def pmx_crossover(self, first_parent,second_parent):
        parent1 = self.population[first_parent]
        parent2 = self.population[second_parent]

        offspring = [-1] * len(parent1)
        start = random.randint(0, len(parent1) - 2)
        end = random.randint(start + 1, len(parent1) - 1)
        for i in range(start, end + 1):
            offspring[i] = parent1[i]
        for i in range(start, end + 1):
            if parent2[i] not in offspring:
                j = i
                while offspring[j] != -1:
                    j = parent2.index(parent1[j])
                offspring[j] = parent2[i]
        for i in range(len(parent2)):
            if offspring[i] == -1:
                offspring[i] = parent2[i]
        return offspring 
    ######################## function for EDGE crossover #######################################
    def edge_crossover(self, first_parent, second_parent):
        parent1 = self.population[first_parent]
        parent2 = self.population[second_parent]
        edge_table = {}
        offspring = []
        for i, value in enumerate(parent1):
            if i == 0:
                 edge_table[value] = [parent1[1], parent1[-1], parent2[(parent2.index(value) + 1) % 30], parent2[(parent2.index(value) - 1) % 30]]
            elif i == 29:
                edge_table[value] = [parent1[0], parent1[-2], parent2[(parent2.index(value) + 1) % 30], parent2[(parent2.index(value) - 1) % 30]]
            else:
                edge_table[value] = [parent1[(i + 1) % 30], parent1[(i - 1) % 30], parent2[(parent2.index(value) + 1) % 30], 
                                     parent2[(parent2.index(value) - 1) % 30]]
       
        gene=random.choice(list(edge_table.keys()))
        offspring.append(gene)
        for i in range(29):
            for j in edge_table.values():
                for k in j:
                    if k in offspring:
                        j.remove(k)
            try:
                gene=random.choice(edge_table[gene])
            except:
                for x in edge_table.keys():
                    if x not in offspring:
                        gene=x
            offspring.append(gene)     
        return offspring
    ######################## function for Inversion mutation #######################################
    def inversion_mutation(self, offspring):
        start_point = random.randint(0, len(offspring) // 2 - 1)
        end_point=random.randint(start_point,len(offspring)-1)
        while start_point == end_point:
            end_point = random.randint(start_point,len(offspring)-1)
        inversion_section=offspring[start_point:end_point]
        inversion_section.reverse()
        offspring[start_point:end_point]=inversion_section
        return offspring
    ######################## function for Scramble mutation #######################################
    def scramble_mutation(self, offspring):
        start_point = random.randint(0, len(offspring) // 2 - 1)
        end_point=random.randint(start_point,len(offspring)-1)
        while start_point == end_point:
            end_point = random.randint(start_point,len(offspring)-1)
        scramble_section=offspring[start_point:end_point]
        random.shuffle(scramble_section)
        return offspring
    ######################## function for alternative child with parent #######################################
    
    def alternative(self,parent1,parent2,child):
        choose_parent=random.randint(1,2)
        if choose_parent==1:
            self.population[parent1]=child
        elif choose_parent==2:
            self.population[parent2]=child
    
    ######################## function for choose best trips in population and evaluate its fitness #######################################
    def best_individual(self):
        best_fitness = min(self.fitness_population.values())
        best_solutions = [i for i, fit in self.fitness_population.items() if fit == best_fitness]
        best_solution_index = random.choice(best_solutions)
        best_solution = self.population[best_solution_index]
        return best_solution,best_fitness
    ######################## function for choose worst trips in population and evaluate its fitness #######################################
    def worst_individual(self):
        worst_fitness = max(self.fitness_population.values())
        worst_solutions = [i for i, fit in self.fitness_population.items() if fit == worst_fitness]
        worst_solution_index = random.choice(worst_solutions)
        worst_solution = self.population[worst_solution_index]
        return worst_solution,worst_fitness
    ######################## function for show plot #######################################
   
    def show_plot(self):
        best_fitness_list = []
        worst_fitness_list = []
        generation_list = []
        for key,value in self.save_bwindividual.items():
            best_fitness_list.append(value[0])
            worst_fitness_list.append(value[1])
            generation_list.append(key)
        plt.plot(generation_list, best_fitness_list, label='Best Fitness')
        plt.plot(generation_list, worst_fitness_list, label='Worst Fitness')
        plt.xlabel('Number of Fitness Evaluations')
        plt.ylabel('Fitness Value')
        plt.title('Best and Worst Fitness over Generations')
        plt.legend()
        plt.show()




       


######################## implement iterate on  classes and their functions #######################################
country_instance = Country(10)
distance_matrix = distance_matrix_reader('dataset.txt')
tsp_solver = TSP(country_instance.trips, distance_matrix)
i=0
while i<2000:
    tsp_solver.fitness()
    f_parent, s_parent = tsp_solver.tournament_selection()
    if i%2==0:
        child1 = tsp_solver.pmx_crossover(f_parent, s_parent)
        child1 = tsp_solver.inversion_mutation(child1)
        tsp_solver.alternative(f_parent, s_parent, child1)
    else:
        child2 = tsp_solver.edge_crossover(f_parent, s_parent)
        child2 = tsp_solver.scramble_mutation(child2)
        tsp_solver.alternative(f_parent, s_parent, child2)
       
    best_ind,best_ind_fitness=tsp_solver.best_individual()
    worst_ind,worst_ind_fitness=tsp_solver.worst_individual()
    tsp_solver.save_bwindividual[i]=[best_ind_fitness,worst_ind_fitness]
    i+=1

tsp_solver.show_plot()



        



            
                 
            

            










    