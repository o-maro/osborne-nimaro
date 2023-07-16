#Sub-Solution 1: Student Assessment

# Assess the academic performance of a student based on their subjects and calculate their overall performance.
def assessStudentPerformance(studentName, subjects):
    # Calculate the performance in each subject
    subjectPerformances = calculateSubjectPerformances(subjects)
    
    # Calculate the overall performance by averaging the subject performances
    overallPerformance = calculateOverallPerformance(subjectPerformances)
    
    return overallPerformance

# Determine the resource requirements (e.g., tutoring or study materials) based on the student's academic performance.
def determineResourceRequirements(academicPerformance):
    # Check the academic performance against a threshold to determine the resource requirements
    if academicPerformance < threshold:
        resourceRequirements = ["Tutoring"]
    else:
        resourceRequirements = ["Study materials"]
    
    return resourceRequirements


#Sub-Solution 2: Resource Allocation


# Allocate the appropriate educational resources to each student based on their resource needs and the availability of resources.
def allocateResources(students, availableResources, studentNeeds):
    allocatedResources = {}
    
    for student in students:
        requiredResources = studentNeeds[student]
        
        for resource in requiredResources:
            if resource in availableResources and availableResources[resource] > 0:
                # Allocate the resource to the student
                allocatedResources.setdefault(student, []).append(resource)
                availableResources[resource] -= 1
            else:
                # No available resources of this type
                allocatedResources.setdefault(student, []).append("No available resources")
    
    return allocatedResources

# Update the availability of educational resources after allocating them to students.
def updateResourceAvailability(availableResources, allocatedResources):
    for student, resources in allocatedResources.items():
        for resource in resources:
            if resource != "No available resources":
                availableResources[resource] -= 1


#Sub-Solution 3: Monitoring and Evaluation


# Track the academic progress of each student and determine if they are improving or not.
def trackStudentProgress(students, studentPerformance, baselinePerformance):
    studentProgress = {}
    
    for student in students:
        if student in studentPerformance:
            performance = studentPerformance[student]
            
            if performance > baselinePerformance:
                studentProgress[student] = "Improving"
            else:
                studentProgress[student] = "Not improving"
        else:
            studentProgress[student] = "No data available"
    
    return studentProgress

# Assess the overall effectiveness of the outreach program based on the progress of the students.
def assessProgramEffectiveness(studentProgress):
    numStudents = len(studentProgress)
    numImproving = sum(progress == "Improving" for progress in studentProgress.values())
    
    programEffectiveness = (numImproving / numStudents) * 100
    
    return programEffectiveness


