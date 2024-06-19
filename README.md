# FJE-new
一、类图

  根目录下classpicture.jpg文件。

二、设计模式说明

  1、迭代器模式（Iterator）：用于构建和返回复杂的 JSON 渲染结构，实现了JSONIterator。
 
	2、策略模式（Strategy）：用于提供风格和图标族的策略，在本项目中已实现树形、矩形风格策略以及卡牌、几何符号策略，并通过Context对象实现了对策略的应用。
 
	3、组合模式（Composite）：设计了中间节点（Container）和叶节点（Leaf），在渲染 JSON 结构时，递归地处理中间节点和叶节点。

三、任务完成

	1、必做与选做均已完成，无论是新风格的添加还是新图标族的添加，都可以通过在对应文件夹添加新的策略并在配置文件中添加新的路径实现。

 	2、运行结果截图：位于仓库result文件夹中。

 	3、仓库链接：https://github.com/WS37/FJE-new
