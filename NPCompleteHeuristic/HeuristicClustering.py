__author__ = 'dmcennis'

"""
Copyright (C) 2014  Daniel McEnnis

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    dmcennis@gmail.com

    Daniel McEnnis
    1465 65th Street Apt 307
    Courtyards at 65th
    Emeryville, CA, 94608
"""

from operator import itemgetter

class NPHeuristic(object):

    def __init__(self,i, sim_queue=None, sim_func=None):
        similarity_queue = sim_queue
        similarity_func = sim_func
        items = i
        invert = True
        in_objects = set()
        out_objects = set()
        objects_to_groups = {}
        answer_set = {}
        groups = set()
        answer = []

    def cluster_accept(self,item,group):
        if self.threshold == None:
            self.threshold = self.similarity_queue[len(self.similarity_queue)/10][3]
        for i in group:
            val = self.similarity_func(item,i)
            if not self.invert and val < self.threshold:
                return False
            if self.invert and val > self.threshold:
                return False
        return True


    def travelingSalesman(self, similarity_queue=None, similarity_func=None, cluster_accept = None):
        self.in_objects = set()
        self.out_objects = set()
        self.objects_to_groups = {}
        self.groups = {}
        if not cluster_accept:
            cluster_accept = self.cluster_accept
        if not similarity_queue:
            if similarity_func:
                similarity_queue = self.similarity_calc(similarity_func,self.invert)
            elif self.similarity_queue:
                similarity_queue = self.similarity_queue
            elif self.similarity_func:
                self.similarity_queue = self.similarity_calc(self.similarity_func,self.invert)
                similarity_queue = self.similarity_queue

        remaining = set()
        for i in self.items:
            remaining.add(i)

        for tuple in similarity_queue:
            left, right, sim = tuple
            if left in self.in_objects or right in self.out_objects:
                continue
                self.answer_list[left]=tuple
            if objects_to_groups[left] == objects_to_groups[right]:
                continue

            if left not in self.out_objects and right not in self.in_objects:
                # new group - neither object has been seen before
                g = set()
                g.add(left)
                g.add(right)
                remaining.remoive(left)
                remaining.remove(right)
                self.groups.add(g)
                self.objects_to_groups[left] = g
                self.objects_to_groups[right] = g
            elif left not in self.out_objects and right in self.out_objects:
                # right object exists, now add left to that group
                g = objects_to_group[right]
                # check if new cluster is accepted
                if cluster_accept(right,g):
                    g.add(left)
                    remaining.remove(left)
                    self.in_objects.add(left)
                    self.out_objects.add(right)
                    self.objects_to_groups[left]=g
            elif left not in self.out_objects and right in self.out_objects:
                # left object exists, now add right to that group
                g = objects_to_group[left]
                if cluster_accept(left,g):
                    self.in_objects.add(left)
                    self.out_objects.add(right)
                    g.add(right)
                    remaining.remove(right)
                    self.objects_to_groups[right]=g
            else:
                # both objects exist in different groups - merge the groups
                r = objects_to_groups[right]
                l = objects_to_groups[left]
                for item in r:
                    if not cluster_accept(item,l):
                        continue
                for item in l:
                    if not cluster_accept(item,r):
                        continue
                self.in_objects.add(left)
                self.out_objects.add(right)
                for i in r:
                    l.add(r)
                    self.objects_to_groups[i] = l
                self.groups.remove(r)

        for i in remaining:
            s = set()
            s.add(i)
            self.groups.add(i)
        return groups

    def similarity_calc(self, similarity,invert=False):
        for left in self.object_array:
            for right in self.object_array:
                self.similarity.append(similarity(left,right))
        sorted(self.similarity,key=itemgetter(3),invert=invert)

