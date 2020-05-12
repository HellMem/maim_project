getwd()

setwd("C:/Users/memo_/Documents/Proyectos/Python/maim_project/output")

items <- c("beca", "vales_transporte", "mentoria", "consulta_psicologica","boleto_evento","asesoria_individual", "cursos_remediales", "visita_empresa", "examen", "platica", "viaje_recreativo")
costo <- c(500L,100L, 200L, 400L, 50L, 250L, 2500L, 50L, 100L, 50L, 10L)
beneficio <- c(30L, 5L, 15L, 8L, 10L, 20L, 50L, 3L, 5L, 2L, 10L)

apoyo.estudiantil <- data.frame(
  items = items,
  costo = costo,
  beneficio = beneficio
)

students <- read.csv("risk.csv")

budget <- 227



fitness.generic <- function(x){
  items.cost <- x %*% apoyo.estudiantil$costo
  items.benefit <- x %*% apoyo.estudiantil$beneficio
  if(items.cost  > budget){
    return(0)
  }else{
    return(-items.benefit)
  }
}


candidate.1 <- c(1,0,0,0,0,0,0,0,0,1, 1)
fitness.generic(candidate.1)


ga.tree <- rbga.bin(size = nrow(apoyo.estudiantil), popSize = 200,
                    mutationChance = 0.01,
                    elitism = 20, iters = 250,
                    evalFunc = fitness.generic,
                    verbose = TRUE
                    
)

summary(ga.tree, echo = T)
best <- ga.tree$population[ga.tree$evaluations == min(ga.tree$best),][1,]
best
fitness.generic(best)





