# STAGE 1: Build the code using Maven
FROM maven:3.9.6-eclipse-temurin-17 AS build
WORKDIR /app
# Copy the project files into the container
COPY pom.xml .
COPY src ./src
# Compile the Java code into a .jar file
RUN mvn clean package -DskipTests

# STAGE 2: Run the code
FROM eclipse-temurin:17-jre-jammy
WORKDIR /app
# Grab the compiled .jar file from STAGE 1
COPY --from=build /app/target/*.jar app.jar
# Tell Render which port to listen to
EXPOSE 8080
# Start the Java server
ENTRYPOINT ["java", "-jar", "app.jar"]