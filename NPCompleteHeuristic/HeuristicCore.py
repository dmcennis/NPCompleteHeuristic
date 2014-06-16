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

    def __init__(self, object_array, similarity_queue=None):
        objects = object_array
        similarity = similarity_queue
        invert = True
        in_objects = set()
        out_objects = set()
        objects_to_groups = {}
        answer_set = {}
        groups = set()
        answer = []


    def travelingSalesman(self, similarity_queue=None, similarity_func=None):
        self.in_objects = set()
        self.out_objects = set()
        self.objects_to_groups = {}
        self.groups = {}
        self.answer_list = {}
        if similarity_queue == None and similarity_func == None:
            return []
        if similarity_func != None and similarity_queue == None:
            self.similarity = self.similarity_calc(similarity_func)
        for tuple in similarity_queue:
            left, right, sim = tuple
            if left in self.in_objects or right in self.out_objects:
                continue
                self.answer_list[left]=tuple
            if objects_to_groups[left] == objects_to_groups[right]:
                continue
            self.in_objects.add(left)
            self.out_objects.add(right)
            self.answer_list[left] = tuple
            if left not in self.out_objects and right not in self.in_objects:
                # new group - neither object has been seen before
                g = set()
                g.add(left)
                g.add(right)
                self.groups.add(g)
                self.objects_to_groups[left] = g
                self.objects_to_groups[right] = g
            elif left not in self.out_objects and right in self.out_objects:
                # right object exists, now add left to that group
                g = objects_to_group[right]
                g.add(left)
                self.objects_to_groups[left]=g
            elif left not in self.out_objects and right in self.out_objects:
                # left object exists, now add right to that group
                g = objects_to_group[left]
                g.add(right)
                self.objects_to_groups[right]=g
            else:
                # both objects exist in different groups - merge the groups
                r = objects_to_groups[right]
                l = objects_to_groups[left]
                for i in r:
                    l.add(r)
                    self.objects_to_groups[i] = l
                self.groups.remove(r)
        self.answer.append(self.objects[0])
        for i in range(1,len(self.answer_list)):
            self.answer.append(self.answer_list[self.answer[i-1]][2])



    def similarity_calc(self, similarity,invert=False):
        for left in self.object_array:
            for right in self.object_array:
                self.similarity.append(similarity(left,right))
        sorted(self.similarity,key=itemgetter(3),invert=invert)
