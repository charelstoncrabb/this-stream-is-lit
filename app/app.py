import asyncio

import pandas
import streamlit as st


from redis_wrapper import RedisStreamReader



def main():
    st.set_page_config(layout="wide")
    st.write("""
    # 🔥 🔥 🔥 This Stream is _Lit_ 🔥 🔥 🔥

    ## 🎉 Welcome to my Streaming Data Demo! 🎉

    This basic demo incorporates two of my favorite things: streamlit and Redis Streams!

    Ok, _three_ of my favorite things: plotting live data!!
    
    ### _Enjoy!_
    """
    )

    table_pane, plot_pane = st.columns([4,6])
    with table_pane:
        table_container = st.empty()
    with plot_pane:
        plot_container = st.empty()
        
    asyncio.run(
        update_data_containers(
            plot_container,
            table_container
        )
    )



async def update_data_containers(
    plot_container,
    table_container
):
    redis_client = RedisStreamReader()
    
    while True:
        data: pandas.DataFrame = await redis_client.read_most_recent()

        table_container.dataframe(data)            
        plot_container.line_chart(
            data=data,
            x='timestamp',
            y=('my_int', 'my_float'),
            height=500
        )
            
        await asyncio.sleep(0.01)



if __name__ == "__main__":
    main()


