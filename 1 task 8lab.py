import re
pose_estimation = "[BodyPart:0-(0.56, 0.23) score=0.80 BodyPart:1-(0.57, 0.33) score=0.79 BodyPart:2-(0.52, 0.35) score=0.70 BodyPart:3-(0.46, 0.40) score=0.69 BodyPart:4-(0.36, 0.41) score=0.84 BodyPart:5-(0.61, 0.32) score=0.72 BodyPart:6-(0.61, 0.21) score=0.58 BodyPart:7-(0.59, 0.11) score=0.80 BodyPart:8-(0.56, 0.52) score=0.43 BodyPart:9-(1.00, 0.65) score=0.36 BodyPart:10-(0.60, 0.80) score=0.63 BodyPart:11-(0.59, 0.51) score=0.50 BodyPart:12-(0.56, 0.65) score=0.50 BodyPart:13-(0.53, 0.80) score=0.69 BodyPart:14-(0.55, 0.22) score=0.64 BodyPart:15-(0.57, 0.22) score=0.67 BodyPart:17-(0.60, 0.24) score=0.33]"
pattern = re.compile(r"\(([\d.]+),\s*([\d.]+)\)\s*score=([\d.]+)")
matches = pattern.findall(pose_estimation)    #Using findall to extract data

#Initializing the points and scores lists
points = []
scores = []

#Processing of results
for match in matches:
    x,y,score = match
    points += [float(x), float(y)]  #Adding coordinates to the points list
    scores += [float(score)]    #Adding confidence to the score list

#Displaying the results
print("points =", points)
print("scores = ", scores)