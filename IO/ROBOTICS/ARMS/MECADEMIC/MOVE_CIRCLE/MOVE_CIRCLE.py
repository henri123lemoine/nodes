import logging
from typing import Optional
from flojoy import flojoy, TextBlob
from PYTHON.utils.mecademic_state.mecademic_calculations import getCirclePositions
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle
from PYTHON.utils.mecademic_state.mecademic_helpers import safe_robot_operation


logger = logging.getLogger(__name__)


# @safe_robot_operation
# @flojoy(deps={"mecademicpy": "1.4.0"})
# def MOVE_CIRCLE(
#         ip_address: TextBlob,
#         center_X: Optional[float] = 0.0,
#         center_Y: Optional[float] = 0.0,
#         center_Z: Optional[float] = 0.0,
#         alpha: Optional[float] = 0.0,
#         beta: Optional[float] = 0.0,
#         gamma: Optional[float] = 0.0,
#         radius: Optional[float] = 0.0,
#         revolutions: Optional[float] = 1.0,
# ) -> TextBlob:
#     """
#     The Move circle node moves in a circle relative to a reference plane.

#     Inputs
#     ------
#     ip_address: TextBlob
#         The IP address of the robot arm.

#     Parameters:
#     -------

#     radius: Optional[float]
#         The radius of the circle. If not specified, the default value of 0.0 is used.
#     revolutions: Optional[float]
#         The number of revolutions to make. If not specified, the default value of 1.0 is used.
#     Returns
#     -------
#     ip_address
#         The IP address of the robot arm.

#     """
#     robot = query_for_handle(ip_address)

#     logger.info("Get Pose:")
#     logger.info(robot.GetPose())
#     # logger.info(center_X, center_Y, center_Z, beta, gamma)

#     # set reference frame
#     robot.MoveLin(x=center_X, y=center_Y, z=center_Z,
#                   alpha=alpha, beta=beta, gamma=gamma)

#     positions = getCirclePositions(
#         radius, revolutions, center_X, center_Y, center_Z)
#     for position in positions:
#         robot.MoveLin(x=position[0], y=position[1],
#                       z=position[2], alpha=alpha, beta=beta, gamma=gamma)
#     robot.MoveLin(x=center_X, y=center_Y, z=center_Z,
#                   alpha=alpha, beta=beta, gamma=gamma)

#     return ip_address


@safe_robot_operation
@flojoy(deps={"mecademicpy": "1.4.0"})
def MOVE_CIRCLE(
        ip_address: TextBlob,
        radius: Optional[float] = 0.0,
        revolutions: Optional[float] = 1.0,
) -> TextBlob:
    """
    The Move circle node moves in a circle relative to a reference plane.

    Inputs
    ------
    ip_address: TextBlob
        The IP address of the robot arm.

    Parameters:
    -------
    radius: Optional[float]
        The radius of the circle. If not specified, the default value of 0.0 is used.
    revolutions: Optional[float]
        The number of revolutions to make. If not specified, the default value of 1.0 is used.

    Returns
    -------
    ip_address
        The IP address of the robot arm.

    """
    robot = query_for_handle(ip_address)

    center_X, center_Y, center_Z, alpha, beta, gamma = robot.GetPose()
    logger.info(
        f"{center_X = }, {center_Y = }, {center_Z = }, {beta = }, {gamma = }")

    positions = getCirclePositions(
        radius, revolutions, center_X, center_Y, center_Z)
    for position in positions:
        robot.MoveLin(x=position[0], y=position[1],
                      z=position[2], alpha=alpha, beta=beta, gamma=gamma)
    robot.MoveLin(x=center_X, y=center_Y, z=center_Z,
                  alpha=alpha, beta=beta, gamma=gamma)

    return ip_address
