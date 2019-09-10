class MaxHeap:
	def __init__(self, _max=100000):
		self.heapList = [0] # 正式的堆元素从下标1开始到n，所以结点的左右孩子下标为2 * i, 2 * i + 1 
		self.currentSize = 0
		self.maximum = _max # 堆能存放的最大元素个数

	# 插入元素
	def insert(self, x):
		self.heapList.append(x)
		self.currentSize += 1
		self.shiftUp(self.currentSize) # 传入当前待插入元素的下标
		
		# 如果超过了堆能存放的元素个数，删除堆顶
		if self.currentSize > self.maximum:
			self.delFirst()

		return self.heapList

	# 一直向上调整
	def shiftUp(self, i):

		currentValue = self.heapList[i]
		# 一直往上到i // 2 == 1结束，指向的是父节点的左孩子结点
		while i  // 2 > 0:
			# 当前结点大于父节点的值
			if self.heapList[i // 2] < currentValue:
				self.heapList[i] = self.heapList[i // 2]
				i = i // 2
			else: # 否则满足，不用调整
				break
		# 如果没有调整，i还是指向当前结点
		# 如果调整了一次，此时i已经是除以2的了，是当前结点的父节点，
		# 如果调整了多次，此时i已经是除以多次2，是当前结点的爷爷或者更高的结点
		self.heapList[i] = currentValue
	
	# 一直向下调整，为的是支持删除堆顶操作，将最后一个元素放到堆顶开始向下调整
	# 和左右最大的孩子结点比较，与较大的孩子结点进行值交换
	def shiftDown(self, i):
		currentValue = self.heapList[i]
		# 控制i * 2 <= self.currentSize可以保证进行到最后一个非叶结点
		while i * 2 <= self.currentSize:
			maxChildIndex = self.maxChild(i)
			if self.heapList[i] < self.heapList[maxChildIndex]:
				self.heapList[i], self.heapList[maxChildIndex] = self.heapList[maxChildIndex], self.heapList[i]
				i = maxChildIndex
			else:
				break
		self.heapList[i] = currentValue

	# 返回结点的较大的孩子结点下标
	def maxChild(self, i):
		if 2 * i + 1 > self.currentSize: # 没有右孩子，则只能返回左孩子
			return 2 * i 

		else:
			if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
				return 2 * i + 1
			else:
				return 2 * i

	# 删除第一个元素
	def delFirst(self):
		retVal = self.heapList[1] # 
		if self.currentSize == 1:
			self.currentSize -= 1
			self.heapList.pop()
			return retVal

		self.heapList[1] = self.heapList[self.currentSize] # 将最后一个元素放到根上来
		self.heapList.pop() # 删除最后一个元素
		self.currentSize -= 1
		# 现在根元素是最后一个元素占位的，需要往下调整，使其满足堆的性质
		self.shiftDown(1)
		return retVal

	# 初始化堆
	# 时间复杂度：O(n)
	def heapify(self, _list):
		self.currentSize = len(_list)
		i = len(_list) // 2 # 从第一个非叶子结点开始
		self.heapList = [0] + _list[:]
		print("heap: ", self.heapList)
		
		print("i: ", i)
		while i > 0: # 调整到i == 0结束，最后一个调整的是i == 1
			self.shiftDown(i)	
			print(i)
			i -= 1
		return self.heapList

	# 原地堆排序，注意现在用的是大顶堆
	def heapSortInPlace(self, _list):
		self.heapify(_list)
		while len(self.heapList) > 0:
			self.heapList[1], self.heapList[self.currentSize] = self.heapList[self.currentSize], self.heapList[1]
			self.currentSize -= 1
			self.shiftDown(1) # 和删除堆顶要进行的调整相同
		return self.heapList

heap = MaxHeap()

_list = [3,1,2,5]

print(heap.heapify(_list))

print(heap.insert(4))

# 参考：https://blog.csdn.net/qq_39422642/article/details/79190195