def activity_selection(activities):
    activities.sort(key=lambda x: x[1])

    selected = [activities[0]]

    last_finish = activities[0][1]

    for i in range(1, len(activities)):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]

    return selected


activities = [(1,3), (2,4), (3,5), (0,6), (5,7)]
print(activity_selection(activities))