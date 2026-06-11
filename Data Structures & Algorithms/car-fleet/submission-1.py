class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        cars = dict(sorted(zip(position, speed), reverse=True))
        for p, s in cars.items():
            time = (target - p) / s

            if not fleet:
                fleet.append(time)
                continue
            
            if time > fleet[-1]:
                fleet.append(time)

        return len(fleet)

                
            