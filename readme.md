<html>
    <h2>About the provided code </h2>
    <p>See the <a href="http://en.wikipedia.org/wiki/Three_Musketeers_%28game%29">Wikipedia
        article</a> for the rules of the game.</p>
    <p>The "board" is represented as a list of five lists; each of these lists
      represents a row, and each list contains five elements. The first list
      represents the first row; the first element in each list represents the
      first column. The values in the list must each be one of three things: an
      <code>'M'</code>, representing a Musketeer, an <code>'R'</code>,
      representing one of Cardinal Richelieu's men; and a <code>'-'</code>,
      representing an empty space. <code>board</code> is a
      global variable in this program.</p>
    <p>Directions are given as one of the four strings <code>'left'</code>, <code>'right'</code>,
      <code>'up</code>', and <code>'down'</code>.</p>
    <p>Your job is to complete the program,  both <code>three_musketeers.py</code>
      and <code>test_three_musketeers.py</code>.</p>
    <ul>
      <li>In <code>three_musketeers.py</code>,
        <ul>
          <li>We use a global variable <code>board</code> to store the current state of 
            the game, and all the functions have access to it.
          <li>For some functions, we indicate that their supplied arguments will not necessarily be 
            in correct value ranges (for the other functions, you can assume that they are in 
            the correct ranges). In this case, you must check for the correctness of the arguments
            and raise an exception if this is violated. Also, the corresponding test methods must
            test the calls with the incorrect arguments and verify if the exceptions are raised.
          <li>The <code>pass</code> statement does nothing. You should replace
            every <code>pass</code> statement with actual code. In the beginning, provide stubs, i.e., 
            return some syntactically correct possibly constant values that do not need to be correct
            semantically. Further, as you develop your project, you will replace them with the code
            that works better and better and covers more and more test cases.</li>
        </ul>
      </li>
      <li>In <code>test_three_musketeers.py</code>,
        <ul>
          <li> Call the function <code>set_board(new_board)</code> to get a fresh new
            <code>board</code> before every test. Do that so that the result of one
            test does not depend on what other tests may have done. (You shoud use
            at least two initial test board.)</li>
          <li>The test functions are not complete (some of them are empty). It is your job
          to fill them in with reasonable tests. In the beginning, just make sure that there
          is at least one test in each of the test functions. Further, as you develop the project, increase
          the number of tests. It is your decision which tests and how many to include, but the tests for 
          each function must reflect the variety of its use cases (including exceptions if we
          indicated that the function must raise them). I would expect between 5 and 10 tests for each
          function, depending on how much the function does.</li>
        </ul>
      </li>
    <li> Try not to work on <code>three_musketeers.py</code> and <code>test_three_musketeers.py</code> 
        in isolation and follow the TDD approach. After improving your code, increase test cases for it, 
        then improve it further, etc. 
    </ul>
</html>
