class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = sorted(list(zip(position,speed)), key=lambda pos: pos[0],reverse=True)
        stack = []

        for pos, speed in sorted_cars:
            time = (target - pos) / speed

            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)



