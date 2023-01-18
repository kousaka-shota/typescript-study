export const Practice2 = () => {
  const getcalculate = (num: number): number => {
    return num ** 2;
  };
  const onClickPractice = () => console.log(getcalculate(100));
  return (
    <div>
      <p>練習</p>
      <button onClick={onClickPractice}>練習問題を実行</button>
    </div>
  );
};
