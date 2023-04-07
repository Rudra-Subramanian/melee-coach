import { SyntheticEvent, useEffect, useState } from "react";

interface Options {
  stage: string;
  characterPicked: string;
  charactersAgainst: string;
  minHits: number;
  slippiSource: string;
}

export const Main = () => {
  const [data, setData] = useState<any>();

  const [options, setOptions] = useState<Options>({
    stage: "",
    characterPicked: "",
    charactersAgainst: "",
    minHits: 0,
    slippiSource: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setOptions((prev) => {
      return {
        ...prev,
        [e.target.name]: e.target.value,
      };
    });
  };

  const submitOptions = () => {
    fetch(
      `http://127.0.0.1:5000/${options.stage}/${options.characterPicked}/${options.charactersAgainst}/${options.minHits}/${options.slippiSource}`
    )
      .then((res) => res.json())
      .then((data: { data: Options }) => {
        console.log(data);
        setData(data.data);
      })
      .catch((e) => console.log(e));
  };

  return (
    <>
      <input
        className="border border-sky-500"
        name="stage"
        placeholder="stage"
        value={options.stage}
        onChange={handleChange}
        required
      />
      <input
        className="border border-sky-500"
        name="characterPicked"
        placeholder="characterPicked"
        value={options.characterPicked}
        onChange={handleChange}
        required
      />
      <input
        className="border border-sky-500"
        name="charactersAgainst"
        placeholder="charactersAgainst"
        value={options.charactersAgainst}
        onChange={handleChange}
        required
      />
      <input
        className="border border-sky-500"
        name="minHits"
        placeholder="minHits"
        value={options.minHits}
        onChange={handleChange}
        required
      />
      <input
        className="border border-sky-500"
        name="slippiSource"
        placeholder="slippiSource"
        value={options.slippiSource}
        onChange={handleChange}
        required
      />
      <button
        className="border border-sky-500"
        type="button"
        onClick={submitOptions}
      >
        Submit
      </button>
    </>
  );
};

export default Main;
