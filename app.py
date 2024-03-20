import streamlit as st


print("page reloaded")
st.set_page_config(
    page_title="축구 도감",
    page_icon="./images/korea.png"
)

st.title("나만의 축구 도감")
st.subheader("선수를 하나씩 추가해서 도감을 채워보세요")


type_position_dict = {
    "공격수": "FW",
    "미드필더": "MF",
    "수비수": "DF",
    "골키퍼": "GK",
}


initial_players = [
    {
        "name": "손흥민",
        "types": ["공격수"],
        "camera": "촬영 연도",
        "years": "2022",
        "image_url": "./images/default.png"
    },
    {
        "name": "김민재",
        "types": ["수비수"],
        "camera": "촬영 연도",
        "years": "2022",
        "image_url": "./images/default.png"
    },
    {
        "name": "황희찬",
        "types": ["공격수"],
        "camera": "촬영 연도",
        "years": "2022",
        "image_url": "./images/default.png"
    },
    {
        "name": "이재성",
        "types": ["미드필더"],
        "camera": "촬영 연도",
        "years": "2022",
        "image_url": "./images/default.png"
    },
]

example_player = {
    "name": "조현우",
    "types": ["골키퍼"],
    "camera": "촬영 연도",
    "years": "2022",
    "image_url": "./images/default.png"
}



if "players" not in st.session_state:
    st.session_state.players = initial_players
    


auto_complete = st.toggle("예시 데이터로 채우기")
print("page_reload, auto_complete", auto_complete)
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="선수 이름",
            value=example_player["name"] if auto_complete else ""
        )
    with col2:
        types = st.multiselect(
            label="선수 포지션",
            options=list(type_position_dict.keys()),
            max_selections=1,
            default=example_player["types"] if auto_complete else []
        )
    image_url = st.text_input(
        label="선수 이미지 URL",
        value=example_player["image_url"] if auto_complete else ""
    )
    camera = st.text_input(
        label="촬영",
        value=example_player["camera"] if auto_complete else ""
    )
    years = st.text_input(
        label="연도",
        value=example_player["years"] if auto_complete else ""
    )
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("선수의 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("선수의 포지션을 적어도 한개 선택해주세요.")
        else:
            st.success("선수를 추가할 수 있습니다.")
            st.session_state.players.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./images/default.png",
                "camera": camera,
                "years": years
            })


for i in range(0, len(st.session_state.players), 2):
    row_players = st.session_state.players[i:i+2]
    cols = st.columns(2)
    for j in range(len(row_players)):
        with cols[j]:
            player = row_players[j]
            with st.expander(label=f"**{i+j+1}. {player['name']}**"):
                st.subheader(player["name"])
                st.subheader(" / ".join(player["types"]))
                st.image(player["image_url"])
                st.subheader(player["camera"])
                st.subheader(player["years"])
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    print("delete button clicked!")
                    del st.session_state.players[i+j]
                    st.rerun()